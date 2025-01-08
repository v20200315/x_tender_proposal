from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.chains.reduce_chain import reduce_chain
from x_sandbox.graph.state import GraphState


async def generate_final_summarization(state: GraphState) -> Dict[str, Any]:
    logger.info("---GENERATE FINAL SUMMARIZATION (X_SANDBOX)---")
    response = await reduce_chain.ainvoke(
        {"collapsed_summarizations": state["collapsed_summarizations"]}
    )
    return {"final_summarization": response}
