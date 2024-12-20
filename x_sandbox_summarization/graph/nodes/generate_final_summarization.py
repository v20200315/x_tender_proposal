from typing import Any, Dict

from logger_config import logger
from x_sandbox_summarization.graph.chains.reduce_chain import reduce_chain
from x_sandbox_summarization.graph.state import GraphState


async def generate_final_summarization(state: GraphState) -> Dict[str, Any]:
    response = await reduce_chain.ainvoke(state["collapsed_summarizations"])
    logger.info(response)
    return {"final_summarization": response}
