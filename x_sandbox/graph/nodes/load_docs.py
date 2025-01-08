from typing import Any, Dict

from langchain_community.document_loaders import PyPDFLoader

from logger_config import logger
from x_sandbox.graph.state import GraphState


def load_docs(state: GraphState) -> Dict[str, Any]:
    logger.info("---LOAD DOCS (X_SANDBOX)---")
    paths = state["paths"]

    docs = [PyPDFLoader(path).load() for path in paths]
    contents = [page for doc in docs for page in doc]

    return {"contents": contents}
