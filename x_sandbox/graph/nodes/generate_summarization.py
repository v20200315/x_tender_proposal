from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.chains.map_chain import map_chain
from x_sandbox.graph.state import GraphState


async def generate_summarization(state: GraphState) -> Dict[str, Any]:
    logger.info("---GENERATE SUMMARIZATION (X_SANDBOX)---")
    response = await map_chain.ainvoke({"content": state["content"]})
    return {"summarizations": [response]}
