from typing import Any, Dict

from x_content.graph.state import GraphState
from x_content.graph.chains.structure_outline_chain import structure_outline_chain


def structure_outline(state: GraphState) -> Dict[str, Any]:

    print("---STRUCTURE OUTLINE (X_CONTENT)---")
    input_text = state["input_text"]

    response = structure_outline_chain.invoke({"input_text": input_text}).content
    return {"outline_json": response}
