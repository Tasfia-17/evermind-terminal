<div align="center">

<!-- Logo -->
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0f0f1a"/>
      <stop offset="100%" style="stop-color:#1a1a2e"/>
    </linearGradient>
    <linearGradient id="ring" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7c3aed"/>
      <stop offset="100%" style="stop-color:#06b6d4"/>
    </linearGradient>
  </defs>
  <rect width="120" height="120" rx="28" fill="url(#bg)"/>
  <circle cx="60" cy="60" r="44" fill="none" stroke="url(#ring)" stroke-width="3" opacity="0.6"/>
  <circle cx="60" cy="60" r="32" fill="none" stroke="url(#ring)" stroke-width="1.5" opacity="0.3"/>
  <!-- Brain outline -->
  <path d="M48 52 Q44 46 48 42 Q54 38 58 44 Q60 40 64 40 Q70 38 72 44 Q78 42 78 50 Q82 54 78 60 Q80 66 74 68 Q72 74 66 72 Q62 76 58 72 Q52 74 50 68 Q44 66 46 60 Q42 56 48 52Z" fill="none" stroke="#7c3aed" stroke-width="1.8" opacity="0.9"/>
  <!-- Pulse line -->
  <polyline points="36,60 44,60 48,52 52,68 56,56 60,64 64,58 68,60 84,60" fill="none" stroke="#06b6d4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>

# EverMind Terminal

**An AI-powered terminal with long-term semantic project memory**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-GPL%20v3-7c3aed?style=flat-square)](LICENSE)
[![Memory](https://img.shields.io/badge/Memory-EverMemOS-06b6d4?style=flat-square)](https://github.com/EverMind-AI/EverMemOS)
[![Competition](https://img.shields.io/badge/Winner-Memory%20Genesis%202026-f59e0b?style=flat-square)]()

*Winner of the Memory Genesis Competition 2026, Track 1: Agent + Memory*

</div>

---

## Table of Contents

- [The Problem](#the-problem)
- [Our Solution](#our-solution)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Memory Commands](#memory-commands)
- [Privacy and Security](#privacy-and-security)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [License](#license)

---

## The Problem

<div align="center">

<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1e2e"/>
      <stop offset="100%" style="stop-color:#181825"/>
    </linearGradient>
  </defs>
  <!-- Card 1 -->
  <rect x="10" y="10" width="200" height="140" rx="12" fill="url(#cardBg)" stroke="#7c3aed" stroke-width="1.5"/>
  <circle cx="40" cy="42" r="14" fill="#7c3aed" opacity="0.2"/>
  <text x="40" y="47" text-anchor="middle" font-size="16" fill="#7c3aed">?</text>
  <text x="110" y="42" text-anchor="middle" font-size="11" font-weight="bold" fill="#cdd6f4" font-family="monospace">Context Loss</text>
  <text x="110" y="62" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">Every session starts</text>
  <text x="110" y="76" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">from a blank slate.</text>
  <text x="110" y="96" text-anchor="middle" font-size="9" fill="#f38ba8" font-family="monospace">bash_history</text>
  <text x="110" y="110" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">is unstructured noise.</text>

  <!-- Card 2 -->
  <rect x="240" y="10" width="200" height="140" rx="12" fill="url(#cardBg)" stroke="#f59e0b" stroke-width="1.5"/>
  <circle cx="270" cy="42" r="14" fill="#f59e0b" opacity="0.2"/>
  <text x="270" y="47" text-anchor="middle" font-size="16" fill="#f59e0b">!</text>
  <text x="340" y="42" text-anchor="middle" font-size="11" font-weight="bold" fill="#cdd6f4" font-family="monospace">Repeated Errors</text>
  <text x="340" y="62" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">Same bugs debugged</text>
  <text x="340" y="76" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">over and over again.</text>
  <text x="340" y="96" text-anchor="middle" font-size="9" fill="#f38ba8" font-family="monospace">Hours wasted</text>
  <text x="340" y="110" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">on solved problems.</text>

  <!-- Card 3 -->
  <rect x="470" y="10" width="200" height="140" rx="12" fill="url(#cardBg)" stroke="#06b6d4" stroke-width="1.5"/>
  <circle cx="500" cy="42" r="14" fill="#06b6d4" opacity="0.2"/>
  <text x="500" y="47" text-anchor="middle" font-size="16" fill="#06b6d4">+</text>
  <text x="570" y="42" text-anchor="middle" font-size="11" font-weight="bold" fill="#cdd6f4" font-family="monospace">Onboarding Pain</text>
  <text x="570" y="62" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">New members struggle</text>
  <text x="570" y="76" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">with tribal knowledge.</text>
  <text x="570" y="96" text-anchor="middle" font-size="9" fill="#f38ba8" font-family="monospace">Days lost</text>
  <text x="570" y="110" text-anchor="middle" font-size="9" fill="#6c7086" font-family="sans-serif">getting up to speed.</text>
</svg>

</div>

Every terminal session starts with a blank slate. Developers constantly lose operational context:

- "How did we fix that database migration conflict last month?" Hours are lost re-debugging the same issue.
- "What was the exact command sequence for deploying the staging server?" Shell history is an unstructured, unsearchable mess.
- "How do I run this project?" New team members struggle with undocumented onboarding steps and tribal knowledge locked in someone's head.

Traditional terminals are amnesic. They execute commands but never learn from them. There is no mechanism to remember, reason over, or share the operational knowledge accumulated during development.

---

## Our Solution

EverMind Terminal is a memory-augmented terminal agent. It acts as a persistent operational brain for your projects, combining a large language model (Google Gemini) with a structured long-term memory backend (EverMemOS).

It does not just execute commands. After every interaction, it stores the prompt, the generated plan, and the result as a semantic memory. Before every new interaction, it retrieves the most relevant past experiences and injects them into the LLM context. Over time, the terminal becomes progressively smarter about your specific project.


---

## Key Features

<div align="center">

<svg width="680" height="220" viewBox="0 0 680 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="f1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7c3aed;stop-opacity:0.15"/>
      <stop offset="100%" style="stop-color:#7c3aed;stop-opacity:0.05"/>
    </linearGradient>
    <linearGradient id="f2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#06b6d4;stop-opacity:0.15"/>
      <stop offset="100%" style="stop-color:#06b6d4;stop-opacity:0.05"/>
    </linearGradient>
    <linearGradient id="f3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:0.15"/>
      <stop offset="100%" style="stop-color:#10b981;stop-opacity:0.05"/>
    </linearGradient>
    <linearGradient id="f4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:0.15"/>
      <stop offset="100%" style="stop-color:#f59e0b;stop-opacity:0.05"/>
    </linearGradient>
  </defs>
  <!-- Feature 1 -->
  <rect x="10" y="10" width="155" height="200" rx="14" fill="url(#f1)" stroke="#7c3aed" stroke-width="1.5"/>
  <rect x="30" y="30" width="36" height="36" rx="8" fill="#7c3aed" opacity="0.3"/>
  <text x="48" y="54" text-anchor="middle" font-size="20" fill="#7c3aed">&#128269;</text>
  <text x="87" y="90" text-anchor="middle" font-size="10" font-weight="bold" fill="#cdd6f4" font-family="sans-serif">Project</text>
  <text x="87" y="104" text-anchor="middle" font-size="10" font-weight="bold" fill="#cdd6f4" font-family="sans-serif">Archaeology</text>
  <text x="87" y="126" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">Search your entire</text>
  <text x="87" y="140" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">project history with</text>
  <text x="87" y="154" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">natural language.</text>
  <!-- Feature 2 -->
  <rect x="178" y="10" width="155" height="200" rx="14" fill="url(#f2)" stroke="#06b6d4" stroke-width="1.5"/>
  <rect x="198" y="30" width="36" height="36" rx="8" fill="#06b6d4" opacity="0.3"/>
  <text x="216" y="54" text-anchor="middle" font-size="20" fill="#06b6d4">&#129504;</text>
  <text x="255" y="90" text-anchor="middle" font-size="10" font-weight="bold" fill="#cdd6f4" font-family="sans-serif">Memory-Augmented</text>
  <text x="255" y="104" text-anchor="middle" font-size="10" font-weight="bold" fill="#cdd6f4" font-family="sans-serif">Generation</text>
  <text x="255" y="126" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">Past experiences</text>
  <text x="255" y="140" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">injected into every</text>
  <text x="255" y="154" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">LLM prompt.</text>
  <!-- Feature 3 -->
  <rect x="346" y="10" width="155" height="200" rx="14" fill="url(#f3)" stroke="#10b981" stroke-width="1.5"/>
  <rect x="366" y="30" width="36" height="36" rx="8" fill="#10b981" opacity="0.3"/>
  <text x="384" y="54" text-anchor="middle" font-size="20" fill="#10b981">&#128274;</text>
  <text x="423" y="90" text-anchor="middle" font-size="10" font-weight="bold" fill="#cdd6f4" font-family="sans-serif">Privacy-Aware</text>
  <text x="423" y="104" text-anchor="middle" font-size="10" font-weight="bold" fill="#cdd6f4" font-family="sans-serif">Storage</text>
  <text x="423" y="126" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">Secrets auto-redacted</text>
  <text x="423" y="140" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">before anything</text>
  <text x="423" y="154" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">leaves your machine.</text>
  <!-- Feature 4 -->
  <rect x="514" y="10" width="155" height="200" rx="14" fill="url(#f4)" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="534" y="30" width="36" height="36" rx="8" fill="#f59e0b" opacity="0.3"/>
  <text x="552" y="54" text-anchor="middle" font-size="20" fill="#f59e0b">&#9889;</text>
  <text x="591" y="90" text-anchor="middle" font-size="10" font-weight="bold" fill="#cdd6f4" font-family="sans-serif">Persistent</text>
  <text x="591" y="104" text-anchor="middle" font-size="10" font-weight="bold" fill="#cdd6f4" font-family="sans-serif">Across Sessions</text>
  <text x="591" y="126" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">Memory survives</text>
  <text x="591" y="140" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">restarts, switches,</text>
  <text x="591" y="154" text-anchor="middle" font-size="8.5" fill="#9399b2" font-family="sans-serif">and reboots.</text>
</svg>

</div>

### Project Archaeology

EverMind Terminal indexes every command you run, every error you encounter, and every solution you apply. It uses semantic search via EverMemOS to let you ask natural language questions about your project history.

```
terminai> recall "database migration error"

On 2026-02-20, you ran `flask db upgrade` and encountered an alembic version conflict.
You resolved it by downgrading to version abc123 with `flask db downgrade abc123`,
then running `flask db upgrade` again.
```

### Memory-Augmented Command Generation

Before the LLM generates a plan for any new command, EverMind Terminal queries EverMemOS for the top semantically relevant past memories. These are injected directly into the Gemini prompt as context. The agent reasons with the accumulated knowledge of your project history rather than starting from scratch.

### Proactive Suggestions

The agent learns your workflow patterns and can suggest the next logical step based on what you and your team have done in similar situations before.

### Privacy-Aware Memory Storage

Sensitive data such as API keys, passwords, tokens, and long base64 strings is automatically redacted by the `privacy_filter` module before any content is sent to EverMemOS.

### Persistent Across Sessions

Memory survives terminal restarts, project switches, and machine reboots. Because EverMemOS stores memories in a persistent backend, your project operational knowledge accumulates indefinitely.

---

## Technology Stack

<div align="center">

<svg width="620" height="80" viewBox="0 0 620 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pill" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#1e1e2e"/>
      <stop offset="100%" style="stop-color:#181825"/>
    </linearGradient>
  </defs>
  <!-- Python -->
  <rect x="10" y="20" width="80" height="40" rx="20" fill="url(#pill)" stroke="#3776AB" stroke-width="1.5"/>
  <text x="50" y="45" text-anchor="middle" font-size="10" fill="#3776AB" font-family="monospace" font-weight="bold">Python 3.10+</text>
  <!-- Gemini -->
  <rect x="105" y="20" width="80" height="40" rx="20" fill="url(#pill)" stroke="#4285F4" stroke-width="1.5"/>
  <text x="145" y="45" text-anchor="middle" font-size="10" fill="#4285F4" font-family="monospace" font-weight="bold">Gemini Pro</text>
  <!-- EverMemOS -->
  <rect x="200" y="20" width="90" height="40" rx="20" fill="url(#pill)" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="245" y="45" text-anchor="middle" font-size="10" fill="#7c3aed" font-family="monospace" font-weight="bold">EverMemOS</text>
  <!-- Supabase -->
  <rect x="305" y="20" width="80" height="40" rx="20" fill="url(#pill)" stroke="#3ECF8E" stroke-width="1.5"/>
  <text x="345" y="45" text-anchor="middle" font-size="10" fill="#3ECF8E" font-family="monospace" font-weight="bold">Supabase</text>
  <!-- PyQt5 -->
  <rect x="400" y="20" width="70" height="40" rx="20" fill="url(#pill)" stroke="#41CD52" stroke-width="1.5"/>
  <text x="435" y="45" text-anchor="middle" font-size="10" fill="#41CD52" font-family="monospace" font-weight="bold">PyQt5</text>
  <!-- uv -->
  <rect x="485" y="20" width="55" height="40" rx="20" fill="url(#pill)" stroke="#06b6d4" stroke-width="1.5"/>
  <text x="512" y="45" text-anchor="middle" font-size="10" fill="#06b6d4" font-family="monospace" font-weight="bold">uv</text>
  <!-- pytest -->
  <rect x="555" y="20" width="55" height="40" rx="20" fill="url(#pill)" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="582" y="45" text-anchor="middle" font-size="10" fill="#f59e0b" font-family="monospace" font-weight="bold">pytest</text>
</svg>

</div>

| Component | Technology |
|---|---|
| Core Language | Python 3.10+ |
| LLM Integration | Google Gemini Pro via `google-generativeai` |
| Long-Term Memory | EverMemOS (local Docker instance or Cloud API) |
| Local Database | Supabase (command history and session state) |
| User Interface | PyQt5 terminal emulator |
| Package Management | uv |
| Testing | pytest |


---

## Project Structure

```
EverMindTerminal/
├── src/
│   ├── main.py                   # Application entry point, PyQt5 UI, Worker thread
│   └── backups/                  # Incremental development snapshots
├── memory/
│   ├── evermem_client.py         # EverMemOS API wrapper (store + semantic search)
│   └── privacy_filter.py         # Redacts secrets before storing to memory
├── Model_json/
│   └── model_json.py             # Gemini prompt builder with memory_context injection
├── generation_models/
│   └── model_1..7.py             # Command generators and executors
├── json_parsing/
│   ├── categoriser.py            # Classifies LLM output into operation types
│   └── parser.py                 # Parses structured JSON plans from LLM responses
├── sequencer/
│   └── sequencer.py              # Manages ordered execution of multi-step plans
├── concat_model/
│   └── concat.py                 # Aggregates and formats multi-model outputs
├── utils/
│   ├── sanitizer/sanitise.py     # Input sanitization before LLM processing
│   ├── setup/                    # Setup scripts, SQL schema, system commands
│   └── test/                     # Test files
├── address.py                    # Address book and project context registry
├── pyproject.toml                # Project dependencies (uv-managed)
├── .env.template                 # Environment variable template
└── LICENSE                       # GNU GPL v3.0
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager (`pip install uv`)
- Docker (for running EverMemOS locally)
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- A Supabase project from [supabase.com](https://supabase.com) (optional, for cloud history)

### Step 1 -- Start EverMemOS Locally

EverMind Terminal requires a running EverMemOS instance for memory storage and retrieval.

```bash
git clone https://github.com/EverMind-AI/EverMemOS.git
cd EverMemOS
docker compose up -d
uv sync
uv run python src/run.py
```

Verify it is running:

```bash
curl http://localhost:1995/health
```

### Step 2 -- Clone and Configure

```bash
git clone https://github.com/Tasfia-17/evermind-terminal.git
cd evermind-terminal
cp .env.template .env
```

Edit `.env` and fill in your credentials:

```env
API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
EVERMEM_BASE_URL="http://localhost:1995/api/v1"
EVERMEM_API_KEY="YOUR_EVERMEMOS_API_KEY"
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_KEY"
PROJECT_ID="my-project"
TEAM_ID="my-team"
```

### Step 3 -- Install and Run

```bash
uv sync
uv run python src/main.py
```

---

## How It Works

<div align="center">

<svg width="680" height="340" viewBox="0 0 680 340" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="nodeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1e2e"/>
      <stop offset="100%" style="stop-color:#181825"/>
    </linearGradient>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#6c7086"/>
    </marker>
  </defs>

  <!-- Step nodes -->
  <!-- 1: User Input -->
  <rect x="270" y="10" width="140" height="44" rx="10" fill="url(#nodeBg)" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="340" y="28" text-anchor="middle" font-size="9" fill="#7c3aed" font-family="monospace" font-weight="bold">1. USER INPUT</text>
  <text x="340" y="44" text-anchor="middle" font-size="8" fill="#9399b2" font-family="sans-serif">Natural language command</text>

  <!-- Arrow down -->
  <line x1="340" y1="54" x2="340" y2="74" stroke="#6c7086" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 2: Memory Retrieval -->
  <rect x="270" y="76" width="140" height="44" rx="10" fill="url(#nodeBg)" stroke="#06b6d4" stroke-width="1.8"/>
  <text x="340" y="94" text-anchor="middle" font-size="9" fill="#06b6d4" font-family="monospace" font-weight="bold">2. MEMORY RETRIEVAL</text>
  <text x="340" y="110" text-anchor="middle" font-size="8" fill="#9399b2" font-family="sans-serif">Semantic search in EverMemOS</text>

  <!-- Arrow down -->
  <line x1="340" y1="120" x2="340" y2="140" stroke="#6c7086" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 3: Context Injection -->
  <rect x="270" y="142" width="140" height="44" rx="10" fill="url(#nodeBg)" stroke="#a855f7" stroke-width="1.8"/>
  <text x="340" y="160" text-anchor="middle" font-size="9" fill="#a855f7" font-family="monospace" font-weight="bold">3. CONTEXT INJECTION</text>
  <text x="340" y="176" text-anchor="middle" font-size="8" fill="#9399b2" font-family="sans-serif">Memories injected into prompt</text>

  <!-- Arrow down -->
  <line x1="340" y1="186" x2="340" y2="206" stroke="#6c7086" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 4: Plan Generation -->
  <rect x="270" y="208" width="140" height="44" rx="10" fill="url(#nodeBg)" stroke="#4285F4" stroke-width="1.8"/>
  <text x="340" y="226" text-anchor="middle" font-size="9" fill="#4285F4" font-family="monospace" font-weight="bold">4. PLAN GENERATION</text>
  <text x="340" y="242" text-anchor="middle" font-size="8" fill="#9399b2" font-family="sans-serif">Gemini outputs JSON plan</text>

  <!-- Arrow down -->
  <line x1="340" y1="252" x2="340" y2="272" stroke="#6c7086" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 5: Execution -->
  <rect x="270" y="274" width="140" height="44" rx="10" fill="url(#nodeBg)" stroke="#10b981" stroke-width="1.8"/>
  <text x="340" y="292" text-anchor="middle" font-size="9" fill="#10b981" font-family="monospace" font-weight="bold">5. EXECUTION</text>
  <text x="340" y="308" text-anchor="middle" font-size="8" fill="#9399b2" font-family="sans-serif">Worker thread runs commands</text>

  <!-- EverMemOS side box -->
  <rect x="490" y="76" width="160" height="242" rx="12" fill="#1e1e2e" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="6,3"/>
  <text x="570" y="100" text-anchor="middle" font-size="9" fill="#7c3aed" font-family="monospace" font-weight="bold">EverMemOS</text>
  <text x="570" y="118" text-anchor="middle" font-size="8" fill="#6c7086" font-family="sans-serif">Semantic Memory Store</text>
  <!-- memory blobs -->
  <rect x="510" y="130" width="120" height="22" rx="6" fill="#2a2a3e" stroke="#7c3aed" stroke-width="1" opacity="0.7"/>
  <text x="570" y="145" text-anchor="middle" font-size="7.5" fill="#cdd6f4" font-family="monospace">memory: flask db error fix</text>
  <rect x="510" y="160" width="120" height="22" rx="6" fill="#2a2a3e" stroke="#7c3aed" stroke-width="1" opacity="0.7"/>
  <text x="570" y="175" text-anchor="middle" font-size="7.5" fill="#cdd6f4" font-family="monospace">memory: deploy sequence</text>
  <rect x="510" y="190" width="120" height="22" rx="6" fill="#2a2a3e" stroke="#7c3aed" stroke-width="1" opacity="0.7"/>
  <text x="570" y="205" text-anchor="middle" font-size="7.5" fill="#cdd6f4" font-family="monospace">memory: cors fix 2026-01</text>
  <rect x="510" y="220" width="120" height="22" rx="6" fill="#2a2a3e" stroke="#06b6d4" stroke-width="1" opacity="0.9"/>
  <text x="570" y="235" text-anchor="middle" font-size="7.5" fill="#06b6d4" font-family="monospace">+ new memory stored</text>

  <!-- Arrows to/from EverMemOS -->
  <line x1="410" y1="98" x2="490" y2="140" stroke="#06b6d4" stroke-width="1.2" stroke-dasharray="4,2" marker-end="url(#arrow)"/>
  <text x="452" y="112" text-anchor="middle" font-size="7" fill="#06b6d4" font-family="sans-serif">search</text>
  <line x1="490" y1="230" x2="410" y2="296" stroke="#10b981" stroke-width="1.2" stroke-dasharray="4,2" marker-end="url(#arrow)"/>
  <text x="452" y="270" text-anchor="middle" font-size="7" fill="#10b981" font-family="sans-serif">store</text>
</svg>

</div>

EverMind Terminal follows a continuous loop: **Retrieve, Reason, Execute, Remember**.

1. **User Input** -- You type a natural language command or question into the terminal UI.
2. **Memory Retrieval** -- The `evermem_client` queries EverMemOS using hybrid semantic search for the top 3 most relevant past memories.
3. **Context Injection** -- Retrieved memories are formatted and injected into the Gemini prompt as prior context alongside the current input and system state.
4. **Plan Generation** -- Gemini generates a structured JSON operation plan containing one or more shell commands, categorized by type.
5. **Parsing and Sequencing** -- The `json_parsing` and `sequencer` modules parse the plan and queue operations in the correct execution order.
6. **Execution** -- A secure Python `Worker` thread executes each command in a subprocess, capturing stdout and stderr.
7. **Memory Formation** -- The original prompt, the generated plan, the command output, and the success status are stored back into EverMemOS as a new episodic memory scoped to your `PROJECT_ID`.
8. **Display** -- The terminal UI renders the output in real time.

---

## Memory Commands

| Command | Description |
|---|---|
| `recall "cors error"` | Semantic search of past memories matching the query |
| `remember "this project uses pyenv + poetry"` | Manually store a project fact or note |
| Any other natural language prompt | Full agent loop: memories retrieved, plan generated, executed, result stored |

---

## Privacy and Security

The `memory/privacy_filter.py` module runs before any content is sent to EverMemOS. It automatically redacts:

- API keys and tokens (detected by common patterns and prefixes)
- Passwords appearing in command arguments
- Long base64-encoded strings
- Environment variable values that match secret patterns

Redacted content is replaced with a placeholder so the memory remains useful for context without exposing sensitive data. All redaction happens locally before any network call is made.

---

## Testing

```bash
pip install pytest
pytest utils/test/
```

Test coverage includes:

- **Command execution logic** -- Verifying the `Worker` class correctly parses and runs sequential command plans.
- **JSON parsing** -- Testing the categoriser and parser against valid and malformed LLM outputs.
- **Memory integration** -- Mocking the EverMemOS client to test storage and retrieval logic in isolation.
- **Terminal UI** -- Basic interaction tests for the PyQt5 terminal emulator.
- **Error handling** -- Ensuring failed commands are captured, displayed, and stored correctly.

---

## Roadmap

<div align="center">

<svg width="620" height="60" viewBox="0 0 620 60" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="30" x2="590" y2="30" stroke="#313244" stroke-width="2"/>
  <!-- Nodes -->
  <circle cx="80"  cy="30" r="10" fill="#7c3aed" opacity="0.9"/>
  <circle cx="210" cy="30" r="10" fill="#06b6d4" opacity="0.9"/>
  <circle cx="340" cy="30" r="10" fill="#10b981" opacity="0.9"/>
  <circle cx="470" cy="30" r="10" fill="#f59e0b" opacity="0.9"/>
  <circle cx="570" cy="30" r="10" fill="#f38ba8" opacity="0.9"/>
  <!-- Labels -->
  <text x="80"  y="52" text-anchor="middle" font-size="7.5" fill="#9399b2" font-family="sans-serif">Web Dashboard</text>
  <text x="210" y="52" text-anchor="middle" font-size="7.5" fill="#9399b2" font-family="sans-serif">Voice Commands</text>
  <text x="340" y="52" text-anchor="middle" font-size="7.5" fill="#9399b2" font-family="sans-serif">Local LLM Support</text>
  <text x="470" y="52" text-anchor="middle" font-size="7.5" fill="#9399b2" font-family="sans-serif">Team Memory Sync</text>
  <text x="570" y="52" text-anchor="middle" font-size="7.5" fill="#9399b2" font-family="sans-serif">Memory Controls</text>
</svg>

</div>

- **Web Dashboard** -- A browser-based GUI to visualize project memory, browse error history, and manage team knowledge.
- **Voice Commands** -- Natural speech input for hands-free terminal control.
- **Local LLM Support** -- Option to use models such as Llama 3 or Mistral locally for full offline privacy.
- **Team Memory Sync** -- Shared EverMemOS namespace so all team members benefit from each other's discoveries and fixes.
- **Granular Memory Controls** -- Per-project and per-command rules for what gets stored, retained, or deleted.

---

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for full details.

---

<div align="center">

<svg width="400" height="50" viewBox="0 0 400 50" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footerLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7c3aed;stop-opacity:0"/>
      <stop offset="50%" style="stop-color:#06b6d4;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#7c3aed;stop-opacity:0"/>
    </linearGradient>
  </defs>
  <line x1="0" y1="25" x2="400" y2="25" stroke="url(#footerLine)" stroke-width="1.5"/>
  <text x="200" y="44" text-anchor="middle" font-size="9" fill="#6c7086" font-family="monospace">built with memory, for developers who remember</text>
</svg>

</div>
