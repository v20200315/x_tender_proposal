from typing import Any, Dict

from logger_config import logger
from x_sandbox_3.graph.chains.generate_keywords_chain import generate_keywords_chain
from x_sandbox_3.graph.state import GraphState


def generate_keywords(state: GraphState) -> Dict[str, Any]:
    logger.info("---GENERATE KEYWORDS (X_SANDBOX_3)---")

    response = generate_keywords_chain.invoke(
        {
            "final_summarization": state["final_summarization"],
            "classification": state["classification"],
        }
    )
    logger.info(response)

    return {"keywords": response}
