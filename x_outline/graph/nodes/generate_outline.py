import os
from typing import Any, Dict

from logger_config import logger
from x_outline.graph.chains.generate_outline_chain import get_generate_outline_chain
from x_outline.graph.chains.generate_outline_chain2 import get_generate_outline_chain2
from x_outline.graph.chains.generate_outline_chain3 import get_generate_outline_chain3
from x_outline.graph.state import GraphState


def generate_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---GENERATE OUTLINE (X_OUTLINE)---")
    llm_type = os.getenv("LLM_TYPE")
    summarizations = state["summarizations"]

    # response = get_generate_outline_chain(llm_type).invoke(
    #     {"summarizations": summarizations, "tier": 1}
    # )
    #
    # response2 = get_generate_outline_chain2(llm_type).invoke(
    #     {"summarizations": summarizations, "outline": response}
    # )
    #
    # response3 = get_generate_outline_chain2(llm_type).invoke(
    #     {"summarizations": summarizations, "outline": response2}
    # )
    #
    # return {"outline": response3}

    response = get_generate_outline_chain3(llm_type).invoke(
        {"summarizations": summarizations, "tier": 3}
    )

    return {"outline": response}
