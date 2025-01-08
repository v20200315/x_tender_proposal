import json
from time import sleep

import streamlit as st
from langchain.memory import ConversationBufferMemory
from langgraph.checkpoint.memory import MemorySaver

from logger_config import logger
from x_sandbox_2.graph.graph import app

# with open("sandbox2.json", "r") as file:
#     data = json.load(file)
#     st.session_state["response_1"] = {
#         "outline": data,
#     }

st.set_page_config(page_title="沙箱步骤二")

if "response_1" in st.session_state:
    response_1 = st.session_state["response_1"]

    if "memory" not in st.session_state:
        st.session_state["memory"] = MemorySaver()
        st.session_state["messages"] = [
            {"role": "ai", "content": response_1["outline"], "type": "json"},
            {"role": "ai", "content": "你好，上述是生成的大纲，你有什么建议吗？如果没有请键入‘满意’两字。", "type": "text"}
        ]

    for message in st.session_state["messages"]:
        if message["type"] == "json":
            with st.chat_message(message["role"]):
                with st.container(height=500):
                    formatted_json = json.dumps(message["content"], indent=4, ensure_ascii=False)
                    st.code(formatted_json, wrap_lines=True, language="json")
        elif message["type"] == "text":
            st.chat_message(message["role"]).write(message["content"])

    feedback = st.chat_input()

    if feedback:

        if feedback.strip() == "满意":
            st.switch_page("sandbox3.py")

        st.session_state["messages"].append({"role": "human", "content": feedback, "type": "text"})
        st.chat_message("human").write(feedback)

        with st.spinner("AI正在思考中，请稍等..."):
            response = app.invoke(
                input={
                    "final_summarization": response_1["final_summarization"],
                    "requirements": response_1["requirements"],
                    "outline": response_1["outline"],
                    "feedback": feedback,
                },
                config={"recursion_limit": 128},
            )
            st.session_state["response_2"] = response
        if response["tasks"]:
            msg = {"role": "ai", "content": response["outline"], "type": "json"}
            st.session_state["messages"].append(msg)
            with st.chat_message("ai"):
                with st.container(height=500):
                    formatted_json = json.dumps(response["outline"], indent=4, ensure_ascii=False)
                    st.code(formatted_json, wrap_lines=True, language="json")
            st.chat_message("assistant").write("反馈结果是否符合您的要求，符合的话请键入‘满意’两字，如不符合可继续反馈。")
        else:
            msg = {"role": "ai", "content": "请输入合适的反馈", "type": "text"}
            st.session_state["messages"].append(msg)
            st.chat_message("ai").write("请输入合适的反馈")

else:
    st.page_link("sandbox.py", label="大纲生成1.1", icon="☕")
