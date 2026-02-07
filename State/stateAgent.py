from langgraph.graph.message import add_messages
from typing import TypedDict , Annotated , Literal , Sequence , Tuple

from langchain_core.messages import BaseMessage
from pydantic import BaseModel , Field


class stateAgent(TypedDict):
    topic:str
    agent11_agent:str
    agent12_agent:str
    agent13_agent:str
    websearch_result:str
    research_result:str
    wiki_result:str
    analysis_report:str
    evaluter:Literal["approval" , "needs_improvement"]
    feedback:str
    optimizer_result:str
    iteration:int
    messages: Annotated[Sequence[BaseMessage] , add_messages]
    user_message: str
    mode:Literal["Research" , "Chat"]
    history: Sequence[Tuple[str, str]]


class stracture_output(BaseModel):
    mode:Literal["Research" , "Chat"] = Field(... , description="decide user want to chat or research")
    topic:str = Field(... , description="specify the topic of research")
    agent11_agent:str = Field(..., description="task for agent 1 which is Collect current trends, industry adoption, and recent discussions")
    agent12_agent:str = Field(..., description="task for agent 2 which is Analyze research papers from past to present evolution")
    agent13_agent:str = Field(..., description="task for agent 3 which is Explain foundational concepts and definitions")


class evaluator_state(BaseModel):
    evaluator:Literal["approval" , "needs_improvement"] = Field(... , description="Final evaluation result.")
    feedback: str = Field(..., description="feedback for the tweet.")