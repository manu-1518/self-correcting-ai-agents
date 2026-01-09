# 🧠 Self-Correcting Multi-Agent AI Research System

A full-stack, local-first AI application where multiple intelligent agents collaborate to research, critique, and refine content. The system runs entirely on **local LLMs** (no API keys, no cloud costs) and includes a **FastAPI backend** with a simple, user-friendly **web frontend**.

---

## 🌟 Highlights

* 🤖 Multi-agent AI workflow (Researcher, Critic, Editor)
* 🔁 Controlled self-correction loops (no infinite recursion)
* 💻 Runs fully offline using Ollama (Gemma 2B)
* ⚡ FastAPI backend with REST endpoint
* 🌐 Clean, simple web frontend
* 🧠 Optimized for low-memory machines
* 🧩 Modular and extensible design

---

## ℹ️ Overview

This project demonstrates how **multiple AI agents** can collaborate in a structured pipeline to produce higher-quality research output.

Instead of relying on a single prompt, the system uses specialized agents with distinct roles:

* **Researcher** creates an initial draft
* **Critic** reviews the draft for major factual or logical issues
* **Editor** refines the content into a polished final report

The system runs for a **controlled number of refinement loops** to improve quality while guaranteeing termination.

All language models are hosted **locally** using **Ollama**, making the project:

* Cost-free
* Privacy-friendly
* Fully offline
* Easy to run on personal machines

---



## 🛠️ Tech Stack

| Component           | Tool                       |
| ------------------- | -------------------------- |
| LLM                 | Ollama (Gemma 2B)          |
| Agent Orchestration | LangGraph                  |
| Backend             | FastAPI + Uvicorn          |
| Frontend            | HTML + JavaScript          |
| Language            | Python 3.11                |
| Environment         | Virtual Environment (venv) |

---

## 📁 Project Structure

```
self_correcting_agents/
│
├── agents/
│   ├── researcher.py
│   ├── critic.py
│   └── editor.py
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── graph.py
├── main.py
├── README.md
├── .gitignore
└── venv/
```

---

## ⚙️ How It Works

```
User → Web UI → FastAPI → LangGraph Agents → Final Report → UI
```

Agent pipeline:

```
Researcher → Critic → (Repeat a few times) → Editor → Final Output
```

This ensures better quality output while preventing infinite loops.

---

## 🚀 Usage

1. Enter a topic in the web interface
2. Click **Generate Report**
3. The system runs the multi-agent pipeline
4. A refined research report is returned

The interface is intentionally simple so users can focus on the results.

---

## ⬇️ Installation

### 1. Install Ollama

[https://ollama.com](https://ollama.com)

### 2. Pull the model

```bash
ollama pull gemma:2b
```

### 3. Start Ollama

```bash
ollama run gemma:2b
```

### 4. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install langgraph langchain langchain-ollama fastapi uvicorn python-multipart ddgs
```

### 6. Run the backend

```bash
uvicorn backend.app:app --reload
```

### 7. Open the frontend

Open:

```
frontend/index.html
```

---



## ✍️ Author

**Manasvi**
AI & Software Engineering Enthusiast

---

