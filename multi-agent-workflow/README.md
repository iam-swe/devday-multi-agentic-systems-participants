# Multi-Agent Workflow — Exam Helper

A clean, minimal multi-agentic system built with **LangGraph** and **Google Gemini**.

---

## 🏗️ Architecture & How It Works

**One LangGraph node. Two agents as tools. Zero extra complexity.**

1. User sends a message.
2. The **OrchestratorAgent** (a LangGraph ReAct agent) reads the message and decides which tool to call:
   - **`explainer`**: Provides simple explanations, analogies, and is beginner-friendly.
   - **`learner`**: Provides in-depth, exam-ready structured study material.
3. The chosen tool runs the corresponding agent and returns the response.
4. The workflow stores conversation history for multi-turn context.

```text
User Message
     │
     ▼
┌─────────────────────────────────────────────────┐
│           Orchestrator Agent (ReAct)            │
│                                                 │
│   ┌──────────────┐   ┌──────────────────────┐   │
│   │   explainer  │   │       learner        │   │
│   │    (tool)    │   │       (tool)         │   │
│   └──────────────┘   └──────────────────────┘   │
└─────────────────────────────────────────────────┘
     │
     ▼
Final Response
```

---

## 📂 Project Structure

| File | Role |
|------|------|
| `multi_agentic_workflow.py` | LangGraph graph definition (`START → orchestrator → END`) |
| `agents/orchestrator_agent.py` | Orchestrator with ReAct loop, holds explainer & learner as tools |
| `agents/explainer_agent.py` | Explains concepts simply (beginner-friendly) |
| `agents/learner_agent.py` | Provides exam-ready structured study material |
| `main.py` | Interactive CLI entry point |

---

## ⚙️ Setup & Installation

### 1. Create and Activate Virtual Environment

**macOS / Linux:**
```bash
uv venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
uv venv
.\.venv\Scripts\Activate.ps1
```
*(If blocked, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` before activating)*

**Windows (Command Prompt):**
```cmd
uv venv
.\.venv\Scripts\activate.bat
```

### 2. Install Dependencies

```bash
uv sync
# Or manually with pip:
# pip install -e .
```

### 3. Environment Variables Setup

Copy the example configuration file:

**macOS / Linux:**
```bash
cp .env.example .env
```

**Windows:**
```cmd
copy .env.example .env
```

Add your API keys to the `.env` file:
```ini
GEMINI_API_KEY=your_google_ai_studio_key
FIRECRAWL_API_KEY=your_firecrawl_key
```

- **Gemini API Key:** Get it from [Google AI Studio](https://aistudio.google.com/app/apikey).
- **Firecrawl API Key:** Get it from [Firecrawl](https://www.firecrawl.dev).

### 4. IDE Setup (VS Code Recommended)

To select the virtual environment, press Ctrl/Cmd + Shift + P, select Python: Select Interpreter and pick the one from .venv

---

## 🚀 Running the Application

### Standard Run

To start the interactive CLI Exam Helper system, run:
```bash
python main.py
```

### Running with Notion MCP Server (Optional)

If you want to use the Notion MCP integration, follow these additional steps:

**1. Configure Notion Credentials**
- Obtain your Notion API token from [Notion Integrations](https://www.notion.so/profile/integrations/internal).
- Inside your Notion workspace, create a new page.
- Under the page's connections, add the connection to your Notion MCP integration.
- Add the following variables to your `.env` file:
```ini
MCP_AUTH_TOKEN=mysecret123         # Choose any secure token
PARENT_PAGE_ID=your_parent_page_id # ID of your connected Notion page
```

**2. Start the Notion MCP Server (Terminal 1)**
In a new terminal window, start the server (replace `your_notion_token` with your actual token):
```bash
NOTION_TOKEN="your_notion_token" npx @notionhq/notion-mcp-server \
  --transport http \
  --port 3000 \
  --auth-token "mysecret123"
```
*(Ensure the `--auth-token` matches the `MCP_AUTH_TOKEN` in your `.env` file)*

**3. Run the Main Application (Terminal 2)**
In your original terminal (with the virtual environment activated), start the app:
```bash
python main.py
```