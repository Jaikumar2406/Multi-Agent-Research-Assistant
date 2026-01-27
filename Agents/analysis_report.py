from State.stateAgent import stateAgent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
combine_llm_api_key =os.getenv("combine_llm")

combine_llm = ChatGroq(model ="llama-3.3-70b-versatile",api_key=combine_llm_api_key, temperature=0.7)



def analysis_report(state: stateAgent):

    web = state.get("websearch_result", "")
    research = state.get("research_result", "")
    wiki = state.get("wiki_result", "")

    if not any([web, research, wiki]):
        return {"analysis_report": ""}

    prompt = f"""
You are an analytical research synthesis agent.

You are given multiple analytical inputs related to the same topic.
Each input may contain overlapping ideas, unique insights, or complementary perspectives.

Your task:
- Carefully read all inputs.
- Identify shared themes and reinforcing ideas.
- Preserve unique, high-value insights.
- Remove redundancy and resolve contradictions.
- Integrate everything into ONE coherent, logically flowing academic research report.
- Maintain analytical depth and conceptual clarity.

Strict report structure (use continuous paragraphs, no headings formatting):

Introduction
Provide background, motivation, scope, and context of the topic.

Consolidated Analysis
Deliver a deep, integrated synthesis of all concepts, methods, findings, and perspectives.

Key Observations
Highlight important patterns, implications, and conceptual takeaways.

Limitations or Open Issues
Analyze unresolved challenges, gaps, or open questions.

Conclusion
Provide a strong, comprehensive conclusion tying everything together.

Length requirement:
- 700 to 1000 words.
- Every paragraph must add meaningful analytical value.

Rules:
- Do NOT mention sources, tools, agents, or inputs.
- Do NOT use bullet points, numbering, or markdown.
- Write in formal academic tone.
- Output ONLY the final report.

Input 1:
{web}

Input 2:
{research}

Input 3:
{wiki}
"""

    response = combine_llm.invoke(prompt)

    return {
        "analysis_report": response.content
    }