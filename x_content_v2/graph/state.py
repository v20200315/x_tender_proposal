import json
from typing import List, TypedDict

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    project_name: str
    outline: str
    todos: List[str]
    summarizations: List[str]
    images: bool
    min_length: int
    article_path: str
