from typing import Any, Dict

from x_sandbox.graph.chains.generate_outline_chain import generate_outline_chain
from x_sandbox.graph.chains.generate_outline_chain2 import generate_outline_chain2
from x_sandbox.graph.state import GraphState


def generate_outline(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE OUTLINE (X_SANDBOX)---")
    summarization = state["summarization"]

    response = generate_outline_chain.invoke(
        {"summarization": summarization, "tier": 1}
    )

    response2 = generate_outline_chain2.invoke(
        {"summarization": summarization, "outline": response}
    )

    response3 = generate_outline_chain2.invoke(
        {"summarization": summarization, "outline": response2}
    )

    import json

    print(json.dumps(response3, indent=2, ensure_ascii=False))

    return {"outline": response3}
