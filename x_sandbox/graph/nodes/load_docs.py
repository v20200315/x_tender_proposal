from typing import Any, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from logger_config import logger
from x_sandbox.graph.state import GraphState


def load_docs(state: GraphState) -> Dict[str, Any]:
    logger.info("---LOAD DOCS (X_SANDBOX)---")
    paths = state["paths"]

    docs = [PyPDFLoader(path).load() for path in paths]
    docs_list = [item for sublist in docs for item in sublist]

    # 文本分割
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=100
    )
    documents = text_splitter.split_documents(docs_list)

    return {"documents": documents}
