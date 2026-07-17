# 🪄 Spellbook

> A modular knowledge engine for capturing, translating, organizing, and exploring ideas.

Spellbook is a collection of Bash and Python tools that transforms small pieces of information ("Quarks") into a searchable knowledge base. It combines command-line automation, desktop utilities, AWS Translate, SQLite, and visualization tools to build a personal knowledge system.

## Features

- 📚 Store knowledge as reusable Quarks
- 🌍 Translate text using AWS Translate
- 🗄 Persist data in SQLite
- 🖥 Desktop GUI applications with Tkinter
- 🔤 Generate word permutations
- ☁ Generate word clouds
- 🐚 Bash automation
- 🐍 Python utilities
- 📈 Foundation for AI-powered knowledge systems

## Architecture

```text
           User
             │
     ┌───────┴────────┐
     │                │
 Bash CLI         Python GUI
     │                │
     └───────┬────────┘
             │
      AWS Translate
             │
             ▼
       SQLite Database
       (whispers.db)
             │
     ┌───────┼────────┐
     │       │        │
Permutations WordCloud Future AI
             │
             ▼
      Personal Knowledge
```

## Repository Structure

```text
spellbook/
├── spellbook          # Bash translation utility
├── secret_ark.py      # Knowledge capture GUI
├── perm_guy.py        # Word permutation generator
├── mind-map.py        # Word cloud visualization
├── whispers.db        # SQLite knowledge database
├── docs/              # Research and notes
└── images/            # Generated diagrams
```

## Technologies

- Python
- Bash
- SQLite
- AWS Translate
- Tkinter
- jq
- WordCloud
- Matplotlib

## Vision

Spellbook is designed as the foundation of a personal Knowledge Operating System. Every idea can be captured, translated, organized, visualized, and eventually connected with AI-assisted search and reasoning.

Future plans include:

- Semantic search
- Local LLM integration (Ollama)
- Embeddings
- Automatic tagging
- Graph visualization
- Markdown/PDF export
- Voice interface
- RichMack Improvement Framework (RIF) integration

---

**Author:** N. J. Franklin  
*Linux • Automation • AI • Knowledge Engineering*
