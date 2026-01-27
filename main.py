from graph import build_workflow
workflow = build_workflow()

input_state = {
    "user_message": "i want to do research on aerodynamics",
    "iteration": 0
}

result = workflow.invoke(
    input_state,
    config={
        "configurable": {
            "thread_id": "user-1"
        }
    }
)

print(result)