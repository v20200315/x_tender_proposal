import os
from typing import Any, Dict

from logger_config import logger
from x_outline.graph.chains.summarize_docs_chain import get_summarize_docs_chain
from x_outline.graph.state import GraphState


def summarize_docs(state: GraphState) -> Dict[str, Any]:
    logger.info("---SUMMARIZE DOCS (X_OUTLINE)---")
    llm_type = os.getenv("LLM_TYPE")
    documents = state["documents"]

    summarizations = []
    for i in range(0, len(documents), 3):
        chunk = documents[i : i + 3]
        response = get_summarize_docs_chain(llm_type).invoke(chunk)
        summarizations.append(response["output_text"])

    return {"summarizations": summarizations}
