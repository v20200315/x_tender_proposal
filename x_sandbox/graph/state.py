from typing import TypedDict, Annotated, List
from langchain_core.documents import Document
import operator


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    paths: List[str]
    contents: List[Document]
    content: Document
    summarizations: Annotated[list, operator.add]
    collapsed_summarizations: List[Document]
    final_summarization: str
    classification: str
    requirements: Annotated[list, operator.add]
    outline: str
