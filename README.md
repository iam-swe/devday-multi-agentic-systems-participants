# 📘 Setup Guide

This repository contains the complete code for the Fifth Elephant workshop "Crafting multi-Agent systems that think and act"

## 📁 Project Structure

- **`conditional-routing`**: A simple agentic workflow demonstrating conditional routing in LangGraph.
- **`multi-agent-workflow`**: A minimal multi-agentic system built with LangGraph and Google Gemini acting as an Exam Helper.

Follow the steps below to set up the project on Windows or macOS.

## ⚙️ Prerequisites

- Python 3.11 – 3.13 recommended

- Git

- A code editor (VS Code recommended)

Check Python version:

```
python --version
```

### 📦 1. Clone the Repository
```
git clone https://github.com/Mahita07/hasgeek-agentic-workshop-blr.git
cd hasgeek-agentic-workshop-blr
```

### 🚀 2. Install uv (Fast Python package manager)
#### macOS
```
brew install uv
```

OR

#### Windows
```
pip install uv
```

#### Windows (PowerShell)
```
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


Restart the terminal after installation.

Verify:

```
uv --version
```


If not recognized:

```
setx PATH "%LOCALAPPDATA%\Programs\uv;%PATH%"
```

Restart terminal again.

### 🐍 3. Use a Compatible Python Version

Some packages may not support very new Python versions.

We pin Python for consistency:

```
uv python install 3.13
uv python pin 3.13
```

## 🛠️ Troubleshooting
❌ uv not found

Restart the terminal or re-add it to PATH.

❌ Python version incompatible

Run:

```
uv python pin 3.13
uv sync
```

❌ PowerShell blocks venv activation

Run:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```