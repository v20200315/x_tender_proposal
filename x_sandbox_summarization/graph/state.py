from typing import TypedDict, Annotated, List
from langchain_core.agents import AgentAction
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage
import operator


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    paths: List[str]
    contents: List[str]
    content: str
    summarizations: Annotated[list, operator.add]
    collapsed_summarizations: List[Document]
    final_summarization: str
