from State.stateAgent import stateAgent
from langchain_groq import ChatGroq
from State.stateAgent import stracture_output

from dotenv import load_dotenv
import os
load_dotenv()
agent1_llm_api_key =os.getenv("agent1_llm")

agent1_llm = ChatGroq(model="llama-3.3-70b-versatile" ,api_key = agent1_llm_api_key , temperature=0.7)

agent_llm1 = agent1_llm.with_structured_output(stracture_output)

def planner_agent(state: stateAgent):

    user_input = state.get("user_message", "")

    prompt = f"""
You are a planning agent.

Decide whether the user wants NORMAL CHAT or RESEARCH.

If the user is asking to:
- explain
- clarify
- simplify
- summarize
existing concepts
→ choose CHAT.

If the user is asking to:
- deeply study
- analyze broadly
- explore a topic in depth
- perform research
→ choose RESEARCH.

If RESEARCH:
- Extract a concise topic (2–5 words).
- Create tasks for THREE agents.

Rules:
- Decide semantically, not by keywords.
- Return ONLY structured output.
"""

    response= agent_llm1.invoke(
        prompt + f"\nUser message:\n{user_input}"
    )

    if response.mode == "Chat":
        return {
            "mode": "Chat"
        }

    return {
        "mode": "Research",
        "topic": response.topic,
        "agent11_agent": response.agent11_agent,
        "agent12_agent": response.agent12_agent,
        "agent13_agent": response.agent13_agent,
    }