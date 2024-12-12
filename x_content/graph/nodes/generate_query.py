from typing import Any, Dict

from x_content.graph.state import GraphState
from x_content.graph.chains.generate_query_chain import generate_query_chain


def generate_query(state: GraphState) -> Dict[str, Any]:

    print("---GENERATE QUERY (X_CONTENT)---")
    summarization = state["summarization"]
    outline_json = state["outline_json"]

    response = generate_query_chain.invoke(
        {"outline_json": outline_json, "summarization": summarization}
    ).content
    # import json
    #
    # print(json.dumps(json.loads(response), indent=2, ensure_ascii=False))
    return {"outline_json": response}
