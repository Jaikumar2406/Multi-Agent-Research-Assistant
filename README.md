
A sophisticated autonomous research and information retrieval system built on LangGraph and Large Language Models (LLMs) that combines the power of multi-agent collaboration with Retrieval-Augmented Generation (RAG) for intelligent information processing and response generation.

## 🌟 Overview

This system represents a cutting-edge approach to automated research and knowledge synthesis, designed to handle complex information needs through a network of specialized AI agents. The architecture dynamically switches between two primary modes:

- **Research Mode**: For in-depth investigation of topics using multiple specialized agents
- **Chat Mode**: For natural language interactions using context from previous research

The system's unique strength lies in its ability to self-evaluate and optimize its outputs, ensuring high-quality, accurate, and well-structured information delivery.


---

## 🚀 Core Capabilities

### 🔍 Intelligent Mode Selection
- **Automatic Context Detection**: Determines the appropriate response strategy (research or chat) based on user input
- **Dynamic Workflow Routing**: Seamlessly transitions between different processing pipelines as needed

### 🤖 Specialized Agent Ecosystem

**🧭 Planner Agent**
- Acts as the central decision-maker and orchestrator
- Analyzes user intent and routes requests appropriately
- Manages the research scope and coordinates agent collaboration
- Implements iterative refinement based on evaluation feedback

**🔍 Research Agents**
- **Web Agent**: Specializes in retrieving current trends, news, and industry-specific information
- **Research Agent**: Focuses on academic papers, technical documentation, and in-depth analysis
- **Wikipedia Agent**: Provides foundational knowledge and contextual background information

### 🧠 Knowledge Processing Pipeline

**Analysis & Synthesis Engine**
- Integrates information from multiple sources into a coherent narrative
- Implements advanced techniques for redundancy removal and conflict resolution
- Maintains source attribution and confidence scoring for all information

**Quality Assurance**
- Automated evaluation of response quality and completeness
- Identification of knowledge gaps and potential inaccuracies
- Continuous improvement through feedback integration

### 🔄 Continuous Improvement

**Optimization Engine**
- Implements multi-dimensional quality assessment (depth, structure, recency, clarity)
- Determines when additional research iterations are needed
- Applies targeted improvements based on evaluation feedback

**Knowledge Management**
- **Vector Database Integration**: Efficient storage and retrieval of research findings
- **Context-Aware Retrieval**: Semantic search capabilities for precise information recall
- **Long-term Memory**: Maintains persistent knowledge across interactions

### 🗂️ State Management & Memory

- **Persistent Context**: Maintains conversation history and research context
- **Thread-based Memory**: Isolates and manages separate conversation threads
- **State Persistence**: Saves and restores system state for long-running tasks
- **Iterative Refinement**: Tracks and builds upon previous research iterations
---

## 🏗️ System Architecture

### Workflow Overview
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


## 🛠️ Technical Stack

### Core Technologies
- **Python**: Primary programming language
- **LangGraph**: Workflow orchestration and state management
- **LangChain**: LLM integration and tooling
- **LLM Backend**: Groq for high-performance inference

### Data Management
- **Vector Database**: Pinecone for efficient similarity search
- **Document Processing**: Advanced text chunking and embedding
- **RAG Architecture**: Integration of retrieval and generation

### Infrastructure
- **FastAPI**: High-performance web framework for the API layer
- **Asynchronous Processing**: For handling concurrent research tasks
- **Modular Design**: Easy extension and customization

## ⚙️ System State Design
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

## 🔄 End-to-End Workflow Example

### Visual Workflow
<img width="716" height="805" alt="Screenshot 2026-01-26 161815" src="https://github.com/user-attachments/assets/b12ef0d7-8b06-4ed1-b175-eb4dac2e7f2b" />
<img width="1906" height="1026" alt="Screenshot 2026-02-08 005315" src="https://github.com/user-attachments/assets/b127e3fb-c240-4e31-a432-58235b557f71" />
<img width="1905" height="1024" alt="Screenshot 2026-02-08 005329" src="https://github.com/user-attachments/assets/e8aaa23f-1542-4961-959f-5824a54ef385" />
<img width="1896" height="950" alt="Screenshot 2026-02-08 005342" src="https://github.com/user-attachments/assets/cffc672e-52b9-43b0-b854-3cc05599fdc7" />


### Scenario: Researching a Technical Topic

1. **Initial Query**
   ```
   User: "Explain the latest advancements in transformer architectures"
   ```

2. **System Processing**
   - Planner Agent identifies need for research
   - Parallel research tasks initiated across specialized agents
   - Results aggregated and analyzed
   - Quality evaluation and potential refinement
   - Final knowledge stored in vector database

3. **Response Generation**
   - Comprehensive, well-structured response generated using RAG
   - Sources and confidence levels included

4. **Follow-up Interaction**
   ```
   User: "How does this compare to previous architectures?"
   ```
   - System retrieves relevant context from previous research
   - Generates informed comparative analysis
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
