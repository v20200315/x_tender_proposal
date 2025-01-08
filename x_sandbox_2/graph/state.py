from typing import TypedDict, List
from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    contents: List[Document]
    copied_contents: List[Document]
    final_summarization: str
    requirements: List[str]
    outline: str
    feedback: str
    tasks: List[str]
    structure_tasks: List[str]
    content_tasks: List[str]
