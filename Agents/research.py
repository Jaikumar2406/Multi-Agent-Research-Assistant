from State.stateAgent import stateAgent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from Agents.search_arxiv import search_arxiv
load_dotenv()

agent3_llm_api_key =os.getenv("agent3_llm")



agent3_llm =ChatGroq(model="llama-3.3-70b-versatile" ,api_key = agent3_llm_api_key , temperature=0.7)


websearch_llm = agent3_llm

def research(state: stateAgent):

    task = state.get("agent12_agent")

    if not task:
        return {"research_result": ""}

    research_summaries = search_arxiv(task)  

    summaries_text = "\n\n".join(
        item["summary"] for item in research_summaries if "summary" in item
    )

    prompt = f"""
You are a research synthesis agent.

Task given by planner:
{task}

You are given multiple research paper summaries below.

Your job:
- Read all summaries carefully.
- Keep only information relevant to the task.
- Remove redundant or overlapping ideas.
- Resolve minor differences by choosing the most consistent viewpoint.
- Combine everything into ONE clear, coherent, meaningful explanation.

Rules:
- Use ONLY the information provided.
- Do NOT fabricate information.
- Do NOT mention papers, tools, or summaries.
- No markdown.
- No bullet points.
- Output ONLY the final explanation.

Research summaries:
{summaries_text}
"""

    response = websearch_llm.invoke(prompt)

    return {
        "research_result": response.content
    }