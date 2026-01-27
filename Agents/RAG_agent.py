from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from State.stateAgent import stateAgent
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage , HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_core.documents import Document


load_dotenv()
RAG_AGENT_api_key =os.getenv("RAG_AGENT")

RAG_AGENT = ChatGroq(model = "llama-3.3-70b-versatile" , api_key=RAG_AGENT_api_key , temperature=0.7)


PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

pc = Pinecone(
    api_key=os.getenv("pine_code_api_key")
)


INDEX_NAME = "research"

if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,  
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )


index = pc.Index(INDEX_NAME)


vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings,
    text_key="text"
)


def ingest_documents_tool(texts: list[str]) -> str:
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

    vectorstore.add_documents(docs)
    return f"Ingested {len(docs)} chunks."


def retrieve_documents_tool(query: str, k: int = 4) -> str:
    """
    Retrieve relevant documents from the vector database for a given query.

    Args:
        query (str): User query
        k (int): Number of relevant chunks to retrieve

    Returns:
        str: Retrieved context text
    """

    docs = vectorstore.similarity_search(query, k=k)

    if not docs:
        return "No relevant information found."

    context = "\n\n".join([doc.page_content for doc in docs])
    return context



def rag_agent(state: stateAgent):
    """
    RAG Agent:
    - Ingest FINAL research content only (once)
    - Answer user queries using retrieved RAG context
    """

    final_content = state.get("analysis_report")

    if (
        final_content
        and isinstance(final_content, str)
        and len(final_content) > 300
    ):
        ingest_documents_tool([final_content])

    system_msg = SystemMessage(content="""
you are a helpful assistant.
use the given context if relevant.
do not mention tools, databases, or internal processes.
""")

    messages = [system_msg]

    user_query = state.get("user_message")

    if user_query:
        context = retrieve_documents_tool(user_query)

        messages.append(
            HumanMessage(content=f"""
context:
{context}

question:
{user_query}
""")
        )
    else:
        messages.append(HumanMessage(content="continue"))

    response = RAG_AGENT.invoke(messages)

    return {
        "messages": [response]
    }