from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.chains.generate_outline_chain import generate_outline_chain
from x_sandbox.graph.state import GraphState


def generate_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---GENERATE OUTLINE (X_SANDBOX)---")

    response = generate_outline_chain.invoke(
        {
            "classification": state["classification"],
            "final_summarization": state["final_summarization"],
            "requirements": state["requirements"],
        }
    )
    return {"outline": response}
