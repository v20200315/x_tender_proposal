from typing import Any, Dict

from logger_config import logger
from x_sandbox_summarization.graph.chains.map_chain import map_chain
from x_sandbox_summarization.graph.state import GraphState


async def generate_summarization(state: GraphState) -> Dict[str, Any]:
    response = await map_chain.ainvoke(state["content"])
    logger.info(response)
    return {"summarizations": [response]}
