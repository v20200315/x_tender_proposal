from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.chains.summarize_docs_chain import summarize_docs_chain
from x_sandbox.graph.state import GraphState


def summarize_docs(state: GraphState) -> Dict[str, Any]:
    logger.info("---SUMMARIZE DOCS (X_SANDBOX)---")
    documents = state["documents"]

    summarizations = []
    for i in range(0, len(documents), 3):
        chunk = documents[i : i + 3]
        response = summarize_docs_chain.invoke(chunk)
        summarizations.append(response["output_text"])

    return {"summarizations": summarizations}
