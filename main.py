
from fastapi import FastAPI, HTTPException
from graph import build_workflow
from database.save_message import save_message
from database.chat_history import get_chat_history
from schemas import ChatRequest, ChatResponse

app = FastAPI(
    title="LangGraph Chat Backend"
)


workflow = build_workflow()


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Backend is running 🚀"}


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    thread_id = payload.thread_id
    user_message = payload.message
    iteration = payload.iteration

    if not user_message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        save_message(thread_id, "user", user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save user message: {e}")

    try:
        history = get_chat_history(thread_id)
    except Exception:
        history = []

    input_state = {
        "user_message": user_message,
        "iteration": iteration,
        "history": history
    }

    try:
        result = workflow.invoke(
            input_state,
            config={
                "configurable": {
                    "thread_id": thread_id
                }
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Workflow error: {e}")

    assistant_reply = "(no response)"
    if "messages" in result and len(result["messages"]) > 0:
        last_message = result["messages"][-1]

        if hasattr(last_message, "content"):
            assistant_reply = last_message.content
        elif isinstance(last_message, dict):
            assistant_reply = last_message.get("content", str(last_message))
        else:
            assistant_reply = str(last_message)

    try:
        save_message(thread_id, "assistant", assistant_reply)
    except Exception:
        pass  # non-blocking

    return ChatResponse(
        thread_id=thread_id,
        reply=assistant_reply,
        iteration=iteration + 1
    )
