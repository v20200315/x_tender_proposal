from typing import Any, Dict

from x_outline.graph.chains.generate_outline_chain import generate_outline_chain
from x_outline.graph.state import GraphState


def generate_outline(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE OUTLINE---")
    documents = state["documents"]

    outline = generate_outline_chain.invoke({"documents": documents})

    # print("generate_outline:")
    # print(outline)
    # print("=" * 20)
    # print(outline.content)
    # print("=" * 20)

    return {"outline": outline.content}
