from typing import Any, Dict

from langchain_core.documents import Document

from x_sandbox_summarization.graph.state import GraphState


def collect_summarizations(state: GraphState) -> Dict[str, Any]:
    return {
        "collapsed_summarizations": [
            Document(summarization) for summarization in state["summarizations"]
        ]
    }
