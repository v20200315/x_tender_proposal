from typing import Any, Dict

from logger_config import logger
from x_outline_v2.graph.chains.generate_outline_chain import generate_outline_chain
from x_outline_v2.graph.chains.generate_outline_chain2 import generate_outline_chain2
from x_outline_v2.graph.state import GraphState


def generate_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---GENERATE OUTLINE (X_OUTLINE)---")
    summarizations = state["summarizations"]

    response = generate_outline_chain.invoke(
        {"summarizations": summarizations, "tier": 1}
    )

    response2 = generate_outline_chain2.invoke(
        {"summarizations": summarizations, "outline": response}
    )

    response3 = generate_outline_chain2.invoke(
        {"summarizations": summarizations, "outline": response2}
    )

    return {"outline": response3}
