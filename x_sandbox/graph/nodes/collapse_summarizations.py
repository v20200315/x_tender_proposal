from typing import Any, Dict

from langchain.chains.combine_documents import split_list_of_docs, acollapse_docs

from logger_config import logger
from x_sandbox.graph.chains.reduce_chain import reduce_chain
from x_sandbox.graph.consts import TOKEN_MAX
from x_sandbox.graph.state import GraphState
from x_sandbox.graph.tools import length_function


async def collapse_summarizations(state: GraphState) -> Dict[str, Any]:
    logger.info("---COLLAPSE SUMMARIZATIONS (X_SANDBOX)---")
    doc_lists = split_list_of_docs(
        state["collapsed_summarizations"], length_function, TOKEN_MAX
    )
    results = []
    for doc_list in doc_lists:
        results.append(await acollapse_docs(doc_list, reduce_chain.ainvoke))

    return {"collapsed_summarizations": results}
