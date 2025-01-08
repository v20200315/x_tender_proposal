from typing import Any, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from logger_config import logger
from x_outline_v2.graph.state import GraphState


def load_docs(state: GraphState) -> Dict[str, Any]:
    logger.info("---LOAD DOCS (X_OUTLINE_V2)---")
    paths = state["paths"]

    docs = [PyPDFLoader(path).load() for path in paths]
    documents = [item for sublist in docs for item in sublist]

    return {"documents": documents}
