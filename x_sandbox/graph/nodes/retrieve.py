from typing import Any, Dict
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from logger_config import logger
from x_sandbox.graph.state import GraphState


def retrieve(state: GraphState) -> Dict[str, Any]:
    logger.info("---RETRIEVE (X_SANDBOX)---")
    question = state["question"]

    retriever = Chroma(
        collection_name="rag-chroma",
        persist_directory="./.chroma",
        embedding_function=OpenAIEmbeddings(),
    ).as_retriever()

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}
