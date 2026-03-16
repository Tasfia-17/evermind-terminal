from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from address import prompts

from dotenv import load_dotenv
from pathlib import Path
import re

NAME = "model_json"

load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

API_KEY = str(os.getenv("API_KEY")).strip()
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def GPT_response(user_prompt, history, username, operating_system, sudo_password, memory_context: str = ""):
    """
    Generates the operation JSON plan.
    memory_context: relevant past memories from EverMemOS, injected into the prompt.
    """
    previous_prompt = history[0].get('Prompt') if history else ""
    previous_result = history[0].get('Results') if history else ""

    memory_section = (
        f"\nRelevant past experiences from memory:\n{memory_context}\n"
        if memory_context else ""
    )

    prompt = prompts.get(NAME).strip() + f"""
                    This is the previous prompt: {previous_prompt}, \n
                    This is the previous result: {previous_result}, \n
                    This is the username: {username}, \n
                    This is the operating system: {operating_system}, \n
                    This is the sudo password: {sudo_password}, \n
                    {memory_section}
                    This is the user's current prompt: {user_prompt}
                """
    try:
        output = ''
        response = chat.send_message(prompt, stream=False, safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE
        })

        if not response:
            raise ValueError("No response received")

        for chunk in response:
            if chunk.text:
                output += str(chunk.text)

        json_list = re.findall('@@@json.*@@@', output, re.DOTALL)
        json_val = re.findall("{.*}", json_list[0].strip(), re.DOTALL)[0].strip()
        return json_val

    except Exception as e:
        print(f"Error in GPT_response: {e}")
        return 'Try again'
