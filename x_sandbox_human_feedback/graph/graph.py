from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import MemorySaver

from x_sandbox_human_feedback.graph.state import GraphState
from x_sandbox_human_feedback.graph.nodes import (
    step_1,
    human_feedback_1,
    step_2,
    human_feedback_2,
    step_3,
)

workflow = StateGraph(GraphState)

workflow.add_node("step_1", step_1)
workflow.add_node("human_feedback_1", human_feedback_1)
workflow.add_node("step_2", step_2)
workflow.add_node("human_feedback_2", human_feedback_2)
workflow.add_node("step_3", step_3)

workflow.add_edge(START, "step_1")
workflow.add_edge("step_1", "human_feedback_1")
workflow.add_edge("human_feedback_1", "step_2")
workflow.add_edge("step_2", "human_feedback_2")
workflow.add_edge("human_feedback_2", "step_3")
workflow.add_edge("step_3", END)

memory = MemorySaver()

app = workflow.compile(checkpointer=memory, interrupt_before=["human_feedback_1", "human_feedback_2"])

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox_human_feedback/graph.png")
