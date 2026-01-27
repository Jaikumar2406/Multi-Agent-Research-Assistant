from State.stateAgent import stateAgent
from langchain_groq import ChatGroq
from Agents.runall import run_all
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

agent2_llm_api_key =os.getenv("agent2_llm")

agent2_llm = ChatGroq(model="llama-3.3-70b-versatile" ,api_key = agent2_llm_api_key , temperature=0.7)

websearch_llm = agent2_llm


def web_search(state: stateAgent):

    task = state.get("agent11_agent")

    if not task:
        return {"websearch_result": ""}

    web_data = asyncio.run(run_all(task))

    prompt = f"""
You are a research execution agent.

Task given by planner:
{task}

Use ONLY the information below.
Do NOT add assumptions.
Do NOT fabricate information.

Web search data:
{web_data}
"""

    response = websearch_llm.invoke(prompt)

    return {
        "websearch_result": response.content
    }