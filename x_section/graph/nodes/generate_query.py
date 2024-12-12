from typing import Any, Dict

from x_section.graph.state import GraphState
from x_section.graph.chains.generate_query_chain import generate_query_chain


def generate_query(state: GraphState) -> Dict[str, Any]:

    print("---GENERATE QUERY (X_SECTION)---")
    documents = state["documents"]
    input_texts = state["input_texts"]
    web_search_queries = []
    for input_text in input_texts:
        response = generate_query_chain.invoke(
            {"input_text": input_text, "documents": documents}
        ).content
        web_search_queries.append(response)

    return {"web_search_queries": web_search_queries}
