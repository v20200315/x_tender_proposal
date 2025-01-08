from typing import Any, Dict

from langchain_core.documents import Document

from logger_config import logger
from x_sandbox.graph.state import GraphState


def collect_summarizations(state: GraphState) -> Dict[str, Any]:
    logger.info("---COLLECT SUMMARIZATIONS (X_SANDBOX)---")
    return {
        "collapsed_summarizations": [
            Document(summarization) for summarization in state["summarizations"]
        ]
    }
