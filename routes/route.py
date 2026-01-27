from State.stateAgent import stateAgent

def route_from_planner(state: stateAgent):
    mode = state.get("mode", "chat")

    if mode == "chat":
        return "chat"

    return "research"

def research_fanout(state: stateAgent):
    """
    Fan-out node.
    the work of this function is to connect research n web and wiki agent to the planner agent.
    """
    return {}

def route(state: stateAgent):
    evaluator = state.get("evaluator")
    iteration = state.get("iteration", 0)

    if evaluator == "Approval" or iteration >= 5:
        return "approve"

    return "needs_improvement"