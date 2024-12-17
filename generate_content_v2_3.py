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

    sections = parsed_json.get("sections", [])

    # 检查 `sections` 是否存在
    if sections:
        # 获取所有标题，用于生成 selectbox 的选项
        section_titles = [section["title"] for section in sections]

        # 使用 selectbox 选择部分
        selected_title = st.selectbox("选择一个部分查看详情", section_titles)

        # 查找选中的部分信息
        selected_section = next(
            (s for s in sections if s["title"] == selected_title), None
        )

        if selected_section:
            # 显示选中部分的摘要
            st.markdown(f"### {selected_section['title']}")
            st.markdown(f"> **摘要：** {selected_section.get('abstract', '无摘要')}")

            # 如果有子部分，递归展示
            if "subsections" in selected_section:
                st.markdown("#### 子部分：")
                for subsection in selected_section["subsections"]:
                    with st.expander(subsection.get("title", "无标题")):
                        st.markdown(
                            f"**摘要：** {subsection.get('abstract', '无摘要')}"
                        )

    else:
        st.error("没有找到 sections 数据！")
