from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from State.stateAgent import stateAgent
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_core.documents import Document

load_dotenv()

RAG_AGENT_api_key = os.getenv("RAG_AGENT")
RAG_AGENT = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=RAG_AGENT_api_key,
    temperature=0.7
)

PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

pc = Pinecone(api_key=os.getenv("pine_code_api_key"))

INDEX_NAME = "research"

if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosign",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings,
    text_key="text"
)


def ingest_documents_tool(texts: list[str]) -> str:
    """Ingest documents into the vector database."""
    try:
        if isinstance(texts, str):
            texts = [texts]

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        docs = []
        for text in texts:
            if not isinstance(text, str) or len(text) < 200:
                continue
            chunks = splitter.split_text(text)
            docs.extend([Document(page_content=c) for c in chunks])

        if docs:
            vectorstore.add_documents(docs)
            return f"Ingested {len(docs)} chunks."
        return "No valid documents to ingest."
    
    except Exception as e:
        return f"Error ingesting documents: {str(e)}"


def retrieve_documents_tool(query: str, k: int = 4) -> str:
    """Retrieve relevant documents from the vector database."""
    try:
        docs = vectorstore.similarity_search(query, k=k)

        if not docs:
            return "No relevant information found."

        context = "\n\n".join([doc.page_content for doc in docs])
        return context
    
    except Exception as e:
        return f"Error retrieving documents: {str(e)}"




from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def rag_agent(state: stateAgent):
    """
    Unified Agent:
    - Uses DB chat history automatically
    - Answers if possible
    - Falls back to analysis / RAG
    """

    update_dict = {}

    user_query = state.get("user_message") or state.get("question")
    history = state.get("history", [])

    # ==========================================================
    # 1️⃣ MEMORY-FIRST (USE DB CHAT HISTORY)
    # ==========================================================

    messages = []

    messages.append(
        SystemMessage(
            content="""
You are a helpful assistant.

You are given the conversation history.
If the user's question can be answered from the history,
answer clearly.

If the history does NOT contain the answer,
reply EXACTLY with:
"I don't know based on the conversation history."
"""
        )
    )

    # inject chat history
    for role, content in history:
        if role == "user":
            messages.append(HumanMessage(content=content))
        else:
            messages.append(AIMessage(content=content))

    # current question
    messages.append(HumanMessage(content=user_query))

    memory_response = RAG_AGENT.invoke(messages)
    memory_answer = memory_response.content.strip()

    # ✅ If memory answered → return immediately
    if "i don't know based on the conversation history" not in memory_answer.lower():
        update_dict["final_answer"] = memory_answer
        update_dict["answer_source"] = "Chat History (DB)"
        update_dict["messages"] = [memory_response]
        return update_dict

    # ==========================================================
    # 2️⃣ ANALYSIS (your existing logic)
    # ==========================================================

    analysis_content = (
        state.get("optimized_report")
        or state.get("analysis_report")
    )

    if analysis_content and len(analysis_content.strip()) > 300:
        system_msg = SystemMessage(content="""
You are presenting a verified research analysis.
Do NOT add new information.
Summarize it briefly and clearly.
""")

        response = RAG_AGENT.invoke([
            system_msg,
            HumanMessage(content=f"""
Analysis Report:
{analysis_content}

User Question:
{user_query}

Task:
Provide a short, clear summary answer.
""")
        ])

        update_dict["final_answer"] = response.content
        update_dict["answer_source"] = "Analysis Summary"
        update_dict["messages"] = [response]
        return update_dict

    # ==========================================================
    # 3️⃣ RAG FALLBACK (your existing logic)
    # ==========================================================

    rag_context = retrieve_documents_tool(user_query) if user_query else ""

    rag_found = (
        rag_context
        and "No relevant information found" not in rag_context
        and len(rag_context.strip()) > 100
    )

    if rag_found:
        system_msg = SystemMessage(content="""
You are answering using retrieved knowledge.
Be accurate and concise.
""")

        response = RAG_AGENT.invoke([
            system_msg,
            HumanMessage(content=f"""
Context:
{rag_context}

Question:
{user_query}

Answer clearly.
""")
        ])

        update_dict["final_answer"] = response.content
        update_dict["answer_source"] = "RAG + LLM"
        update_dict["messages"] = [response]
        return update_dict

    # ==========================================================
    # 4️⃣ FINAL FALLBACK
    # ==========================================================

    update_dict["final_answer"] = "No sufficient information available."
    update_dict["answer_source"] = "Fallback"
    return update_dict
