import json
from time import sleep

import streamlit as st
from langchain.memory import ConversationBufferMemory
from langgraph.checkpoint.memory import MemorySaver

from logger_config import logger

st.set_page_config(page_title="沙箱步骤三")

if "response_2" in st.session_state:
    response_2 = st.session_state["response_2"]

    formatted_json = json.dumps(response_2["outline"], indent=4, ensure_ascii=False)
    st.code(formatted_json, wrap_lines=True, language="json")

else:
    st.page_link("sandbox.py", label="大纲生成1.1", icon="☕")
