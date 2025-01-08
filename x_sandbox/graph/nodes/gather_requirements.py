from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.chains.gather_requirements_chain import gather_requirements_chain
from x_sandbox.graph.state import GraphState


async def gather_requirements(state: GraphState) -> Dict[str, Any]:
    logger.info("---GATHER REQUIREMENTS (X_SANDBOX)---")
    response = await gather_requirements_chain.ainvoke({"content": state["content"]})
    return {"requirements": [response]}
