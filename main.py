# from graph import build_workflow
# from database.save_message import save_message
# from database.chat_history import get_chat_history

# workflow = build_workflow()

# iteration = 0
# thread_id = "user-1"

# print("Ask questions (type 'exit' to stop)\n")

# while True:
#     try:
#         user_message = input("You: ").strip()

#         # Handle empty input
#         if not user_message:
#             print("⚠️  Please enter a message.\n")
#             continue

#         if user_message.lower() == "exit":
#             print("Exiting...")
#             break

#         # 🔥 SAVE USER MESSAGE
#         try:
#             save_message(thread_id, "user", user_message)
#         except Exception as e:
#             print(f"⚠️  Failed to save user message: {e}")

#         # 🔥 FETCH CHAT HISTORY
#         try:
#             history = get_chat_history(thread_id)
#         except Exception as e:
#             print(f"⚠️  Failed to fetch history: {e}")
#             history = []

#         input_state = {
#             "user_message": user_message,
#             "iteration": iteration,
#             "history": history
#         }

#         # 🔥 INVOKE WORKFLOW
#         try:
#             result = workflow.invoke(
#                 input_state,
#                 config={
#                     "configurable": {
#                         "thread_id": thread_id
#                     }
#                 }
#             )
#         except Exception as e:
#             print(f"\n❌ Workflow error: {e}")
#             print("-" * 40)
#             iteration += 1
#             continue

#         # 🔥 EXTRACT ASSISTANT REPLY
#         if "messages" in result and len(result["messages"]) > 0:
#             try:
#                 last_message = result["messages"][-1]
                
#                 # Handle different message formats
#                 if hasattr(last_message, 'content'):
#                     assistant_reply = last_message.content
#                 elif isinstance(last_message, dict):
#                     assistant_reply = last_message.get('content', str(last_message))
#                 else:
#                     assistant_reply = str(last_message)

#                 print("\nAssistant:")
#                 print(assistant_reply)

#                 # 🔥 SAVE ASSISTANT MESSAGE
#                 try:
#                     save_message(thread_id, "assistant", assistant_reply)
#                 except Exception as e:
#                     print(f"⚠️  Failed to save assistant message: {e}")

#             except Exception as e:
#                 print(f"\n❌ Error extracting reply: {e}")
#         else:
#             print("\nAssistant: (no response)")

#         print("-" * 40)
#         iteration += 1

#     except KeyboardInterrupt:
#         print("\n\n👋 Interrupted. Exiting...")
#         break
#     except EOFError:
#         print("\n\n👋 Input closed. Exiting...")
#         break
#     except Exception as e:
#         print(f"\n❌ Unexpected error: {e}")
#         print("-" * 40)
#         iteration += 1










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
