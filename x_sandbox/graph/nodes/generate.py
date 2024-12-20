from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.chains.generate_chain import generate_chain
from x_sandbox.graph.state import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    logger.info("---GENERATE (X_SANDBOX)---")
    question = state["question"]
    documents = state["documents"]

    generation = generate_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}
