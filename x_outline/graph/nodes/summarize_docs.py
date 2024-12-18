from typing import Any, Dict

from logger_config import logger
from x_outline_v2.graph.chains.summarize_docs_chain import summarize_docs_chain
from x_outline_v2.graph.state import GraphState


def summarize_docs(state: GraphState) -> Dict[str, Any]:
    logger.info("---SUMMARIZE DOCS (X_OUTLINE)---")
    documents = state["documents"]

    summarizations = []
    for i in range(0, len(documents), 3):
        chunk = documents[i : i + 3]
        response = summarize_docs_chain.invoke(chunk)
        summarizations.append(response["output_text"])

    return {"summarizations": summarizations}
