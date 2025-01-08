from dotenv import load_dotenv

load_dotenv()

from logger_config import logger
from x_sandbox_human_feedback.graph.graph import app

if __name__ == "__main__":
    thread = {"configurable": {"thread_id": "777"}}

    initial_input = {"input": "hello world"}

    for step in app.stream(initial_input, thread, stream_mode="values"):
        logger.info(step)

    user_input_1 = input("human_feedback_1: ")

    app.update_state(
        thread, {"user_feedback_1": user_input_1}, as_node="human_feedback_1"
    )

    for step in app.stream(None, thread, stream_mode="values"):
        logger.info(step)

    user_input_2 = input("human_feedback_2: ")

    app.update_state(
        thread, {"user_feedback_2": user_input_2}, as_node="human_feedback_2"
    )

    for step in app.stream(None, thread, stream_mode="values"):
        logger.info(step)
