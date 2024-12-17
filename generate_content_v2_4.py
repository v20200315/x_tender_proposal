import json
import os
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="投标文件生成器")
st.markdown("#### 投标文件内容生成器 V0.1.2")


# 将嵌套的 sections 展平为一维列表，包含路径信息
def flatten_sections(sections, parent_path=""):
    flattened = []
    for section in sections:
        # 构造完整路径
        path = f"{parent_path} > {section['title']}".strip(" >")
        flattened.append(
            {
                "path": path,
                "title": section["title"],
                "abstract": section.get("abstract", "无摘要"),
            }
        )
        # 递归处理子部分
        if "subsections" in section:
            flattened.extend(flatten_sections(section["subsections"], path))
    return flattened


if "path" not in st.session_state or "outline" not in st.session_state:
    st.page_link("generate_outline_v2.py", label="首先创建Outline", icon="📋")

else:
    if st.session_state["path"]:
        st.write(st.session_state["path"])

    if st.session_state["outline"]:
        st.json(st.session_state["outline"], expanded=False)

    parsed_json = st.session_state["outline"]

    # 获取所有节点信息
    sections = parsed_json.get("sections", [])
    flat_sections = flatten_sections(sections)

    # 提取所有路径用于 selectbox
    options = [item["path"] for item in flat_sections]

    # 显示 selectbox
    selected_option = st.selectbox("选择一个部分查看详情", options)

    # 查找选中的部分内容
    selected_section = next(
        (item for item in flat_sections if item["path"] == selected_option), None
    )

    if selected_section:
        # 显示选中部分的信息
        st.markdown(f"### {selected_section['title']}")
        st.markdown(f"> **摘要：** {selected_section['abstract']}")
    else:
        st.error("未找到相关信息！")
