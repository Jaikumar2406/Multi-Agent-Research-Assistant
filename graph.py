from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from Agents.analysis_report import analysis_report
from Agents.planner_agent import planner_agent
from Agents.web_agent import web_search
from Agents.research import research
from Agents.evaluation_agent import evaluation_agent
from Agents.wiki_agent import wiki
from Agents.optimizer_agent import optimizer_agent
from Agents.RAG_agent import rag_agent
from routes.route import route , research_fanout , route_from_planner
from State.stateAgent import stateAgent


def build_workflow():
    graph = StateGraph(stateAgent)

    # Nodes
    graph.add_node("planner_agent", planner_agent)
    graph.add_node("research_fanout", research_fanout)
    graph.add_node("web_agent", web_search)
    graph.add_node("research_agent", research)
    graph.add_node("wiki_agent", wiki)
    graph.add_node("analysis_agent", analysis_report)
    graph.add_node("evaluation_agent", evaluation_agent)
    graph.add_node("optimizer_agent", optimizer_agent)
    graph.add_node("RAG_agent", rag_agent)

    # Start
    graph.add_edge(START, "planner_agent")

    # Planner → execution
    graph.add_conditional_edges(
        "planner_agent",
        route_from_planner,
        {
            "chat": "RAG_agent",
            "research": "research_fanout"
        }
    )

    # Fanout
    graph.add_edge("research_fanout", "web_agent")
    graph.add_edge("research_fanout", "research_agent")
    graph.add_edge("research_fanout", "wiki_agent")

    # Execution → analysis
    graph.add_edge("web_agent", "analysis_agent")
    graph.add_edge("research_agent", "analysis_agent")
    graph.add_edge("wiki_agent", "analysis_agent")

    # Analysis → evaluation
    graph.add_edge("analysis_agent", "evaluation_agent")

    # Evaluation → routing
    graph.add_conditional_edges(
        "evaluation_agent",
        route,
        {
            "approve": "RAG_agent",
            "needs_improvement": "optimizer_agent"
        }
    )

    # Loop back
    graph.add_edge("optimizer_agent", "planner_agent")

    # End
    graph.add_edge("RAG_agent", END)

    # Memory + compile
    memory = MemorySaver()
    workflow = graph.compile(checkpointer=memory)

    return workflow
