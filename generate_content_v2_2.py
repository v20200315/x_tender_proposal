import json
import os
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="投标文件生成器")
st.markdown("#### 投标文件内容生成器 V0.1.2")

if "path" not in st.session_state or "outline" not in st.session_state:
    st.page_link("generate_outline_v2.py", label="首先创建Outline", icon="📋")

else:
    if st.session_state["path"]:
        st.write(st.session_state["path"])

    if st.session_state["outline"]:
        st.json(st.session_state["outline"], expanded=False)

    parsed_json = st.session_state["outline"]

    st.header(parsed_json.get("title", "无标题"))

    sections = parsed_json.get("sections", [])
    for idx, section in enumerate(sections):
        st.button(f"生成第{idx + 1}章内容")
        with st.container(height=200):
            formatted_json = json.dumps(section, indent=4, ensure_ascii=False)
            st.code(formatted_json, wrap_lines=True, language="json")
