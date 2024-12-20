from typing import Any, Dict

from langchain_core.documents import Document

from logger_config import logger
from x_sandbox_2.graph.chains.summarize_docs_chain import summarize_docs_chain
from x_sandbox_2.graph.chains.summarize_docs_chain2 import summarize_docs_chain2
from x_sandbox_2.graph.state import GraphState


def summarize_docs(state: GraphState) -> Dict[str, Any]:
    print("---SUMMARIZE DOCS (X_SANDBOX_2)---")
    documents = state["documents"]

    # summarizations = []
    # for i in range(0, len(documents), 3):
    #     chunk = documents[i : i + 3]
    #     response = summarize_docs_chain.invoke(chunk)
    #     summarizations.append(response)
    #
    # response = summarize_docs_chain.invoke(summarizations)
    #
    # logger.info(response)
    #
    # return {"summarization": response}

    summarizations = []
    for i in range(0, len(documents), 3):
        chunk = documents[i: i + 3]
        response = summarize_docs_chain2.invoke(chunk)
        summarizations.append(Document(page_content=response["output_text"]))

    response = summarize_docs_chain2.invoke(summarizations)
    logger.info(response["output_text"])

    return {"summarization": response["output_text"]}
