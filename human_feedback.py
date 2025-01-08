import json
import os

import streamlit as st

from logger_config import logger
from x_sandbox_human_feedback.graph.graph import app

st.markdown("#### 测试Human Feedback")

thread = {"configurable": {"thread_id": "777"}}
initial_input = {"input": "hello world"}

if "反馈1" not in st.session_state:
    st.session_state["反馈1"] = False
if "反馈2" not in st.session_state:
    st.session_state["反馈2"] = False
if "完成" not in st.session_state:
    st.session_state["完成"] = False

with st.form("first_form"):
    if st.form_submit_button("开始"):
        for step in app.stream(initial_input, thread, stream_mode="values"):
            st.write(step)
        st.session_state["反馈1"] = True

if st.session_state["反馈1"]:
    with st.form("second_form"):
        human_feedback_1 = st.text_input("Enter human feedback 1:")
        if st.form_submit_button("反馈1"):
            if human_feedback_1.strip():
                app.update_state(
                    thread,
                    {"user_feedback_1": human_feedback_1},
                    as_node="human_feedback_1",
                )
                for step in app.stream(None, thread, stream_mode="values"):
                    st.write(step)
                st.session_state["反馈2"] = True
            else:
                st.error("Please enter human feedback 1")

if st.session_state["反馈2"]:
    with st.form("third_form"):
        human_feedback_2 = st.text_input("Enter human feedback 2:")
        if st.form_submit_button("反馈2"):
            if human_feedback_2.strip():
                app.update_state(
                    thread,
                    {"user_feedback_2": human_feedback_2},
                    as_node="human_feedback_2",
                )
                for step in app.stream(None, thread, stream_mode="values"):
                    st.write(step)
                st.session_state["完成"] = True
            else:
                st.error("Please enter human feedback 2")

if st.session_state["完成"]:
    st.success("Process Completed!")
