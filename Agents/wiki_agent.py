from State.stateAgent import stateAgent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from Agents.search_wiki import search_wikipedia
load_dotenv()

agent3_llm_api_key =os.getenv("agent3_llm")
agent3_llm =ChatGroq(model="llama-3.3-70b-versatile" ,api_key = agent3_llm_api_key , temperature=0.7)

wiki_llm = agent3_llm

def wiki(state: stateAgent):

    task = state.get("agent13_agent")

    if not task:
        return {"wiki_result": ""}

    wiki_summaries = search_wikipedia(task) 

    summaries_text = "\n\n".join(wiki_summaries)

    prompt = f"""
You are a Wikipedia synthesis agent.

Task given by planner:
{task}

You are given multiple Wikipedia summaries below.

Your job:
- Read all summaries carefully.
- Keep only information relevant to the task.
- Remove redundant or overlapping content.
- Merge everything into ONE clear, coherent, meaningful explanation.

Rules:
- Use ONLY the information provided.
- Do NOT add external knowledge.
- Do NOT mention Wikipedia or tools.
- No markdown.
- No bullet points.
- Output ONLY the final explanation.

Wikipedia summaries:
{summaries_text}
"""

    response = wiki_llm.invoke(prompt)

    return {
        "wiki_result": response.content
    }