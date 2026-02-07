# Autonomous Multi-Agent Research & RAG Assistant

An autonomous research system built using LangGraph, LLMs, and RAG.  
The system intelligently decides between **research mode** and **chat mode**, performs deep multi-agent research, synthesizes knowledge, evaluates quality, optimizes iteratively, and finally enables context-aware chat using RAG.


---

## 🚀 Key Features

**🧭 Planner Agent**

  Automatically detects whether the user wants:
  
  Research (deep investigation)
  
  Normal Chat
  
  Extracts research topic and assigns tasks to agents

**🤖 Multi-Agent Research System**

  Web Agent → current trends & industry adoption
  
  Research Agent → academic papers & evolution
  
  Wikipedia Agent → foundational concepts

**🧪 Analysis & Synthesis**

  Merges all research into a single, coherent analytical report
  
  Removes redundancy and resolves conflicts

**🧠 Evaluation Agent**

  Judges if the research is research-ready
  
  Identifies gaps and weaknesses

**🔁 Optimizer Agent**

  Decides what to improve (depth, structure, recency, clarity)
  
  Triggers another research iteration if needed

**📚 RAG (Retrieval-Augmented Generation)**

  Stores final research in a vector database
  
  Enables high-quality, context-aware chat after research is complete

**🗂️ Persistent Memory**

Uses thread-based memory for multi-turn interactions
---

## 🧠 System Architecture
```
START
  ↓
Planner Agent
  ├─ Chat → RAG Agent → END
  └─ Research
        ↓
    Research Fan-Out
     ├─ Web Agent
     ├─ Research Agent
     └─ Wiki Agent
        ↓
   Analysis Agent
        ↓
  Evaluation Agent
     ├─ Approved → RAG Agent → END
     └─ Needs Improvement → Optimizer Agent → Planner Agent
```
<img width="581" height="763" alt="Screenshot 2026-01-26 161932" src="https://github.com/user-attachments/assets/2a544c56-ab8b-4379-a396-9a84646c7613" />

## 🛠️ Tech Stack

Python

LangGraph

LangChain

LLMs (Groq)

Vector Database (Pinecone)

Recursive Text Chunking

RAG Architecture

## 🧠 State Design
```
class stateAgent(TypedDict):
    user_message: str
    topic: str
    agent11_agent: str
    agent12_agent: str
    agent13_agent: str
    websearch_result: str
    research_result: str
    wiki_result: str
    analysis_report: str
    evaluator: Literal["approval", "needs_improvement"]
    feedback: str
    optimizer_result: str
    iteration: int
    messages: Sequence[BaseMessage]
```

## Example Workflow
```
User input:
"I want to research transformers"

System behavior:
Planner selects research mode.
Agents perform parallel research.
Analysis and evaluation loop runs.
Final knowledge is stored in the vector database.
System switches to RAG chat mode.

Follow-up question:
"Explain self-attention in simple terms"

Answer is generated from stored research using RAG.
```
