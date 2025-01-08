import copy
from typing import Any, Dict

from logger_config import logger
from x_sandbox_2.graph.chains.parse_feedback_chain import parse_feedback_chain
from x_sandbox_2.graph.state import GraphState


def parse_feedback(state: GraphState) -> Dict[str, Any]:
    logger.info("---PARSE FEEDBACK (X_SANDBOX_2)---")

    response = parse_feedback_chain.invoke({"feedback": state["feedback"]})
    logger.info(state["feedback"])
    logger.info(response)
    return {"tasks": response}
