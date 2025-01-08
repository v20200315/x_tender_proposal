from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.chains.classify_summarization_chain import (
    classify_summarization_chain,
)
from x_sandbox.graph.state import GraphState


def classify_summarization(state: GraphState) -> Dict[str, Any]:
    logger.info("---CLASSIFY SUMMARIZATION (X_SANDBOX)---")
    response = classify_summarization_chain.invoke(
        {"final_summarization": state["final_summarization"]}
    )
    return {"classification": response}
