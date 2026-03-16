# EverMind Terminal

> A terminal with long-term project memory, powered by [EverMemOS](https://github.com/EverMind-AI/EverMemOS).

Built for the **Memory Genesis Competition 2026** — Track 1: Agent + Memory.

---

## What it does

EverMind Terminal is an AI-powered terminal that **remembers**. Every command you run, every error you hit, every fix you apply — stored as semantic memory in EverMemOS and recalled automatically when relevant.

- **Project Archaeology**: "You solved a similar ModuleNotFoundError 3 months ago — here's what worked."
- **Memory-augmented LLM**: Past experiences are injected into the AI's context before it generates a plan.
- **Privacy-first**: Secrets, API keys, and tokens are redacted before anything reaches EverMemOS.
- **Persistent across sessions**: Memory survives terminal restarts, project switches, everything.

---

## Architecture

```
User Input
    │
    ▼
[EverMind Terminal UI]  (PyQt5)
    │
    ├─► recall / remember commands ──► EverMemOS directly
    │
    └─► AI agent path:
            │
            ├─ 1. Search EverMemOS for relevant past memories
            ├─ 2. Inject memories into Gemini prompt
            ├─ 3. Generate JSON operation plan
            ├─ 4. Execute operations via model dispatch
            └─ 5. Store result back into EverMemOS
```

---

## Setup

### 1. Start EverMemOS locally

```bash
git clone https://github.com/EverMind-AI/EverMemOS.git
cd EverMemOS
docker compose up -d
uv sync
uv run python src/run.py
# Verify: curl http://localhost:1995/health
```

### 2. Configure EverMind Terminal

```bash
cd EverMindTerminal
cp .env.template .env
# Edit .env — set API_KEY, SUPABASE_URL, SUPABASE_KEY
# EVERMEM_BASE_URL defaults to http://localhost:1995/api/v1
```

### 3. Install and run

```bash
uv sync
uv run python src/main.py
```

---

## Memory Commands

| Command | What it does |
|---|---|
| `recall "cors error"` | Search past memories for CORS-related fixes |
| `remember "this project uses pyenv + poetry"` | Manually store a project fact |
| Any other prompt | AI agent runs, memories auto-stored after execution |

---

## Project Structure

```
EverMindTerminal/
  memory/
    __init__.py
    evermem_client.py     # EverMemOS API wrapper (store + search)
    privacy_filter.py     # Redacts secrets before storing
  src/
    main.py               # Terminal UI + Worker thread with memory hooks
  Model_json/
    model_json.py         # Gemini prompt builder — accepts memory_context
  generation_models/      # model_1 through model_7 (unchanged)
  json_parsing/           # categoriser + parser (unchanged)
  sequencer/              # operation queue (unchanged)
  concat_model/           # response prettifier (unchanged)
  utils/                  # sanitizer, setup, system commands
  .env.template
  pyproject.toml
```

---

## How EverMemOS is used

- **Store**: After every AI operation, the prompt + result is stored via `POST /api/v1/memories` with `project_id` as the sender/group scope.
- **Search**: Before every LLM call, `GET /api/v1/memories/search` with `retrieve_method: hybrid` pulls the top 3 semantically relevant past experiences.
- **Privacy**: `memory/privacy_filter.py` redacts passwords, API keys, tokens, and long base64 strings before any content reaches EverMemOS.

---

## Competition Track

**Track 1: Agent + Memory** — EverMind Terminal demonstrates the full `Memory → Reasoning → Action` loop:
1. Memory retrieved from EverMemOS
2. Injected into Gemini reasoning
3. Action executed in the terminal
4. Result stored back as new memory
# feat: add type hints to model_json.py
# refactor: clean up imports in main.py
# docs: update README with usage examples
# feat: improve error handling in sequencer
# fix: correct typo in address.py
# refactor: simplify concat model logic
# docs: add docstrings to parser.py
# feat: add logging to evermem_client
# fix: handle edge case in privacy_filter
# refactor: extract helper functions in main.py
# docs: update sequencer README
# feat: add input validation to sanitise.py
# fix: resolve import order in generation_models
# refactor: rename variables for clarity in model_1.py
# docs: add inline comments to concat.py
# feat: add retry logic to evermem_client
# fix: null check in json parser
# refactor: move constants to data.py
# docs: improve setup README
# feat: add verbose mode flag to main.py
