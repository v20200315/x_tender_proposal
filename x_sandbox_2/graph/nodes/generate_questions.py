from typing import Any, Dict

from x_sandbox_2.graph.chains.generate_questions_chain import generate_questions_chain
from x_sandbox_2.graph.state import GraphState


def generate_questions(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE QUESTION (X_SANDBOX_2)---")
    summarization = state["summarization"]

    response = generate_questions_chain.invoke({"summarization": summarization})

    print(f"questions: {response.content}")

    return {"questions": response.content}
