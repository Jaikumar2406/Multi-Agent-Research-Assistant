from State.stateAgent import stateAgent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from State.stateAgent import evaluator_state
load_dotenv()
agent1_llm_api_key =os.getenv("agent1_llm")
agent2_llm_api_key =os.getenv("agent2_llm")
agent3_llm_api_key =os.getenv("agent3_llm")
combine_llm_api_key =os.getenv("combine_llm")
evauate_llm1_api_key =os.getenv("evauate_llm1")
optimizer_llm_api_key =os.getenv("optimizer_llm")
RAG_AGENT_api_key =os.getenv("RAG_AGENT")


agent3_llm =ChatGroq(model="llama-3.3-70b-versatile" ,api_key = agent3_llm_api_key , temperature=0.7)
combine_llm = ChatGroq(model ="llama-3.3-70b-versatile",api_key=combine_llm_api_key, temperature=0.7)
evauate_llm1 = ChatGroq(model="llama-3.3-70b-versatile" , api_key=evauate_llm1_api_key, temperature=0.7)
optimizer_llm = ChatGroq(model = "llama-3.3-70b-versatile" , api_key=optimizer_llm_api_key, temperature=0.7)
RAG_AGENT = ChatGroq(model = "llama-3.3-70b-versatile" , api_key=RAG_AGENT_api_key , temperature=0.7)

evauate_llm = evauate_llm1.with_structured_output(evaluator_state)


def evaluation_agent(state: stateAgent):

    analysis = state.get("analysis_report", "")

    if not analysis:
        return {
            "evaluator": "needs_improvement",
            "feedback": "No consolidated analysis was available for evaluation."
        }

    prompt = f"""
You are a research evaluation and gap-analysis agent.

You will be given a consolidated research analysis.

Your task:
- Evaluate whether the analysis is sufficient for high-quality research work.
- Identify gaps, weaknesses, or missing components if any.

Decision rules:
- If the analysis is complete, deep, coherent, and research-ready:
IMPORTANT:
- evaluator must be exactly one of:
  "approval" or "needs_improvement"
- use only lowercase

STRICT OUTPUT FORMAT (no extra text):

Decision: "approval" or "needs_improvement"
Feedback: <concise but clear evaluation and actionable guidance>

Rules:
- Do NOT summarize or rewrite the analysis.
- Do NOT mention tools, agents, or sources.
- Focus only on evaluation and gaps.

Analysis:
{analysis}
"""

    response = evauate_llm.invoke(prompt)

    # 🔒 deterministic parsing
    decision = "needs_improvement"
    feedback = response

    if "Decision: approval" in response:
        decision = "approval"

    return {
        "evaluator": response.evaluator,
        "feedback": response.feedback  
    }