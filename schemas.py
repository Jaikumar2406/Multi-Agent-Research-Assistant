from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    thread_id: str
    message: str
    iteration: Optional[int] = 0


class ChatResponse(BaseModel):
    thread_id: str
    reply: str
    iteration: int
