from State.stateAgent import stateAgent
def optimizer_agent(state: stateAgent):
    """
    Optimizer Agent
    ----------------
    Role:
    - reads Evaluation feedback 
    - Decide wheather need improvement
    - makes Optimization STRATEGY 
    - generate Content
    """

    decision = state.get("evaluator", "needs_improvement")
    feedback = state.get("feedback", "")

    if decision == "approval":
        return {
            "optimization_plan": [],
            "iteration": state.get("iteration", 0)
        }

    optimization_plan = []

    if any(word in feedback for word in ["short", "insufficient", "depth"]):
        optimization_plan.append("increase_research_depth")

    if any(word in feedback for word in ["citation", "source", "reference"]):
        optimization_plan.append("add_more_sources")

    if any(word in feedback for word in ["unclear", "confusing"]):
        optimization_plan.append("clarify_explanation")

    if any(word in feedback for word in ["structure", "organized"]):
        optimization_plan.append("improve_structure")

    if any(word in feedback for word in ["redundant", "repetition"]):
        optimization_plan.append("remove_redundancy")

    if "outdated" in feedback:
        optimization_plan.append("use_recent_information")

    if not optimization_plan:
        optimization_plan.append("minor_refinement")

    iteration = int(state.get("iteration", 0)) + 1

    return {
        "optimization_plan": optimization_plan,
        "iteration": iteration
    }