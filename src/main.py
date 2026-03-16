import sys
import os
import subprocess

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtCore import Qt, QThread, pyqtSignal

import queue

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Model_json.model_json import GPT_response
from json_parsing.categoriser import categorise
from sequencer.sequencer import process_json
from concat_model.concat import concatenate

from generation_models.model_1 import generate_command_1, execute_1
from generation_models.model_2 import generate_command_2, execute_2
from generation_models.model_3 import generate_command_3, execute_3
from generation_models.model_4 import generate_command_4, execute_4
from generation_models.model_5 import generate_command_5, execute_5
from generation_models.model_6 import generate_command_6, execute_6
from generation_models.model_7 import generate_command_7, execute_7

from supabase import create_client, Client
from dotenv import load_dotenv
from pathlib import Path
from utils.setup.data import user_dict
from utils.setup.system_commands import commands_list

# EverMemOS memory client
from memory.evermem_client import EverMemClient

load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

url: str = str(os.getenv("SUPABASE_URL")).strip()
key: str = str(os.getenv("SUPABASE_KEY")).strip()
supabase: Client = create_client(url, key)

PROJECT_ID = os.getenv("PROJECT_ID", "evermind-terminal")
evermem = EverMemClient()


def add_history(user_prompt, categoriser_json, results):
    assert type(results) == list, 'results must be a list'
    if categoriser_json is not None:
        Info = {'Prompt': user_prompt, 'Categorizer_json': categoriser_json, 'Results': results}
    else:
        Info = {'Prompt': user_prompt, 'Results': results}
    supabase.table('History_v3').insert(Info).execute()


def get_history(n):
    return supabase.table('History_v3').select("*").order('id', desc=True).limit(n).execute().data


def _store_memory(prompt: str, results: list):
    """Store the interaction as an episodic memory in EverMemOS (non-blocking best-effort)."""
    try:
        content = f"User: {prompt}\nResult: {results[-1] if results else ''}"
        evermem.store(content, PROJECT_ID)
    except Exception as e:
        print(f"[EverMem] store failed: {e}")


def _recall_memory(prompt: str) -> str:
    """Retrieve relevant past memories for the current prompt."""
    try:
        memories = evermem.search(prompt, PROJECT_ID, top_k=3)
        if memories:
            return "\n".join(f"- {m}" for m in memories)
    except Exception as e:
        print(f"[EverMem] search failed: {e}")
    return ""


class Worker(QThread):
    result_ready = pyqtSignal(list)

    def __init__(self, prompt, parent=None):
        super().__init__(parent)
        self.prompt = prompt

    def run(self):
        try:
            # --- Special memory commands ---
            stripped = self.prompt.strip()

            if stripped.lower().startswith("recall "):
                query = stripped[7:].strip().strip('"')
                memories = _recall_memory(query)
                if memories:
                    self.result_ready.emit([f"🧠 Memory recall for '{query}':\n{memories}"])
                else:
                    self.result_ready.emit(["No relevant memories found."])
                return

            if stripped.lower().startswith("remember "):
                fact = stripped[9:].strip().strip('"')
                _store_memory(f"[manual] {fact}", [fact])
                self.result_ready.emit([f"✅ Stored in memory: {fact}"])
                return

            # --- Direct shell command ---
            if str(self.prompt).split(' ')[0] in commands_list:
                results = []
                if str(self.prompt).split(' ')[0].strip().lower().startswith('cd'):
                    target_dir = self.prompt.split(" ")[1]
                    os.chdir(os.path.expanduser(target_dir))
                    output = f"Changed directory to {os.getcwd()}"
                    results.append(output)
                else:
                    output = subprocess.run(self.prompt, shell=True,
                                            text=True, check=True, capture_output=True)
                    results.append(output.stdout)

                add_history(self.prompt, None, results)
                _store_memory(self.prompt, results)

            else:
                # --- AI agent path ---
                history = get_history(1)
                username = user_dict.get("username")
                operating_system = user_dict.get("operating_system")
                sudo_password = user_dict.get("sudo_password")

                # Retrieve relevant memories BEFORE calling the LLM
                memory_context = _recall_memory(self.prompt)
                if memory_context:
                    print(f"[EverMem] Injecting {len(memory_context.splitlines())} memories into prompt")

                processed_output = GPT_response(
                    user_prompt=self.prompt,
                    history=history,
                    username=username,
                    operating_system=operating_system,
                    sudo_password=sudo_password,
                    memory_context=memory_context,
                )

                categorised_output = categorise(processed_output)
                operations_q = process_json(f"{categorised_output}")
                results = self.execute_queue(operations_q, categorised_output)

                add_history(self.prompt, categorised_output, results)
                _store_memory(self.prompt, results)

        except Exception as e:
            results = [f"Error: {str(e)}"]

        self.result_ready.emit(results)

    def execute_queue(self, operations_q, categorised_output):
        results = []
        model_dispatch = {
            "model_1": ("generation_models.model_1", "generate_command_1", "execute_1"),
            "model_2": ("generation_models.model_2", "generate_command_2", "execute_2"),
            "model_3": ("generation_models.model_3", "generate_command_3", "execute_3"),
            "model_4": ("generation_models.model_4", "generate_command_4", "execute_4"),
            "model_5": ("generation_models.model_5", "generate_command_5", "execute_5"),
            "model_6": ("generation_models.model_6", "generate_command_6", "execute_6"),
            "model_7": ("generation_models.model_7", "generate_command_7", "execute_7"),
        }
        additional_data = ''

        while not operations_q.empty():
            operation = operations_q.get()
            operation_type = operation.get('operation_type')
            model_name = operation.get('model_name')
            parameters = operation.get('parameters')

            if model_name not in model_dispatch:
                results.append(f"Error: Unknown model '{model_name}'.")
                continue

            module_path, generate_func, execute_func = model_dispatch[model_name]
            try:
                model_module = __import__(module_path, fromlist=[generate_func, execute_func])
                generate_command = getattr(model_module, generate_func)
                execute_command = getattr(model_module, execute_func)

                command = generate_command(
                    operation=operation_type,
                    parameters=parameters,
                    additional_data=additional_data,
                )

                if command.strip().startswith("cd "):
                    target_dir = command.split(" ", 1)[1]
                    os.chdir(os.path.expanduser(target_dir))
                    output = f"Changed directory to {os.getcwd()}"
                    concat_output = f"{concatenate(user_prompt=self.prompt, final_output=output)} \n"
                else:
                    if model_name in ['model_1', 'model_2', 'model_3', 'model_4', 'model_5', 'model_7']:
                        output = execute_command(command)
                        concat_output = f"{concatenate(user_prompt=self.prompt, final_output=output)} \n"
                    else:
                        output = command
                        concat_output = f"{concatenate(user_prompt=self.prompt, final_output=output)} \n"

                results.append(concat_output)
                additional_data = output

            except Exception as e:
                results.append(f"Error: {str(e)}")

        return results


class ModernTerminal(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.command_history = []
        self.history_index = -1
        self.is_processing = False
        self.current_prompt = ""

    def init_ui(self):
        mem_status = "🟢 Memory ON" if evermem.health() else "🔴 Memory OFF"
        self.setWindowTitle(f"EverMind Terminal  |  {mem_status}")
        self.setGeometry(100, 100, 900, 550)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.terminal_display = QTextEdit()
        self.terminal_display.setReadOnly(True)
        self.terminal_display.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e2e;
                color: #cdd6f4;
                border: none;
                padding: 4px;
            }
        """)
        self.terminal_display.setFont(QFont("Monospace", 11))

        # Startup banner
        self.terminal_display.append(
            '<span style="color:#89b4fa;">╔══════════════════════════════════════════╗</span>'
        )
        self.terminal_display.append(
            '<span style="color:#89b4fa;">║       EverMind Terminal  v1.0            ║</span>'
        )
        self.terminal_display.append(
            '<span style="color:#89b4fa;">║  Powered by EverMemOS  |  Long-term AI   ║</span>'
        )
        self.terminal_display.append(
            '<span style="color:#89b4fa;">╚══════════════════════════════════════════╝</span>'
        )
        self.terminal_display.append(
            f'<span style="color:#a6e3a1;">{mem_status}  |  Project: {PROJECT_ID}</span>'
        )
        self.terminal_display.append(
            '<span style="color:#6c7086;">  recall "query"  →  search past memories</span>'
        )
        self.terminal_display.append(
            '<span style="color:#6c7086;">  remember "fact" →  store a memory</span>\n'
        )

        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Monospace", 11))
        self.input_field.setStyleSheet("""
            QLineEdit {
                border: 1px solid #45475a;
                border-radius: 3px;
                padding: 2px;
                background-color: #1e1e2e;
                color: #cdd6f4;
            }
        """)
        self.input_field.returnPressed.connect(self.start_processing)

        self.main_layout.addWidget(self.terminal_display, stretch=1)
        self.main_layout.setSpacing(0)
        self.main_layout.addWidget(self.input_field, stretch=0)
        self.setLayout(self.main_layout)
        self.append_prompt()

    def append_prompt(self):
        user = os.getenv("USER", 'user')
        current_dir = os.getcwd()
        home = os.path.expanduser("~")
        if current_dir.startswith(home):
            current_dir = "~" + current_dir[len(home):]

        prompt_text = (
            f'<span style="color:#89b4fa;">{user}</span>'
            f'<span style="color:#6c7086;">@evermind</span>:'
            f'<span style="color:#a6e3a1;">{current_dir}</span>'
            f' <span style="color:#f38ba8;">$</span> '
        )
        self.terminal_display.append(prompt_text)
        self.terminal_display.moveCursor(QTextCursor.End)

    def start_processing(self):
        if self.is_processing:
            return

        self.is_processing = True
        self.current_prompt = self.input_field.text()

        if self.current_prompt.strip():
            if self.current_prompt.strip().lower() == "clear":
                self.terminal_display.clear()
                self.append_prompt()
                self.is_processing = False
                self.input_field.clear()
                return

            self.terminal_display.insertPlainText(self.current_prompt + "\n")
            self.terminal_display.append(
                '<span style="color:#fab387;">⏳ Thinking...</span>'
            )
            self.terminal_display.moveCursor(QTextCursor.End)
            QApplication.processEvents()

            self.worker = Worker(self.current_prompt)
            self.worker.result_ready.connect(self.display_response)
            self.worker.start()

        self.input_field.clear()

    def display_response(self, results):
        cursor = self.terminal_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.select(QTextCursor.LineUnderCursor)
        cursor.removeSelectedText()
        cursor.deletePreviousChar()

        formatted_output = f"\n<span style='color:#89dceb;'>▶</span> {results[-1]} \n"
        self.terminal_display.append(f"<pre>{formatted_output}</pre>")
        self.append_prompt()
        self.is_processing = False


app = QApplication(sys.argv)
terminal = ModernTerminal()
terminal.show()
sys.exit(app.exec_())
