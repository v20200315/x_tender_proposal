import os
from typing import Any, Dict
from langchain_community.tools import TavilySearchResults
from langchain.schema import Document

from logger_config import logger
from x_content.graph.chains.write_draft_chain import get_write_draft_chain
from x_content.graph.state import GraphState

web_search_tool = TavilySearchResults(k=3)


def write_draft(state: GraphState) -> Dict[str, Any]:
    logger.info("---WRITE DRAFT (X_CONTENT)---")
    llm_type = os.getenv("LLM_TYPE")
    project_name = state["project_name"]
    outline = state["outline"]
    todo_list = state["todo_list"]
    done_list = state["done_list"]
    summarizations = state["summarizations"]
    images = state["images"]
    min_length = state["min_length"]

    todo = todo_list.pop(0)

    query = " ".join([project_name, todo["title"], todo["abstract"]])
    docs = web_search_tool.invoke({"query": query})
    web_results = "\n".join([d["content"] for d in docs])
    web_results = Document(page_content=web_results)
    documents = [web_results]

    response = get_write_draft_chain(llm_type).invoke(
        {
            "outline": outline,
            "title": todo["title"],
            "abstract": todo["abstract"],
            "summarizations": summarizations,
            "documents": documents,
            "images": images,
            "min_length": min_length,
        }
    )

    if llm_type == "通义千问":
        todo["content"] = response
    else:
        todo["content"] = response.content

    return {"doing": todo}
