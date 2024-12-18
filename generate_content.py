from datetime import datetime
import streamlit as st

from logger_config import logger
from x_content.graph.graph import app

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
                "subsections": section.get("subsections", []),
            }
        )
        # 递归处理子部分
        # 现阶段只是展示章信息，节信息需要去掉注释
        # if "subsections" in section:
        #     flattened.extend(flatten_sections(section["subsections"], path))
    return flattened


# 递归获取子节点信息
def get_subsections_info(section):
    info = {
        "title": section["title"],
        "abstract": section.get("abstract", "无摘要"),
        "subsections": [],
    }
    if "subsections" in section:
        for child in section["subsections"]:
            info["subsections"].append(get_subsections_info(child))
    return info


# 获取父节点链信息
def get_parent_chain(flat_sections, path):
    chain = []
    parts = path.split(" > ")
    for i in range(len(parts)):
        parent_path = " > ".join(parts[: i + 1])
        parent = next(
            (item for item in flat_sections if item["path"] == parent_path), None
        )
        if parent:
            chain.append(
                {"title": parent["title"], "abstract": parent.get("abstract", "无摘要")}
            )
    return chain


def display_section_info(section, sub_nodes, level=0):
    sub_nodes.append({"title": section["title"], "abstract": section["abstract"]})
    indent = "  " * level
    st.markdown(f"{indent}- **{section['title']}**: {section['abstract']}")
    for subsection in section.get("subsections", []):
        display_section_info(subsection, sub_nodes, level + 1)


# def get_leaf_nodes(section):
#     leaves = []
#     if "subsections" in section and section["subsections"]:
#         for subsection in section["subsections"]:
#             leaves.extend(get_leaf_nodes(subsection))
#     else:
#         leaves.append(
#             {
#                 "title": section["title"],
#                 "abstract": section.get("abstract", "无摘要"),
#             }
#         )
#     return leaves


# def get_path_by_title(flat_sections, target_title):
#     for section in flat_sections:
#         if section["title"] == target_title:
#             return section["path"]
#     return ""


# 假设 parsed_json 已在 session_state 中
if "path" not in st.session_state or "outline" not in st.session_state:
    st.page_link("generate_outline.py", label="首先创建Outline", icon="📋")
else:
    # if st.session_state["path"]:
    #     st.write(st.session_state["path"])

    # if st.session_state["outline"]:
    #     st.json(st.session_state["outline"], expanded=False)

    parsed_json = st.session_state["outline"]

    # 获取项目名称
    project_name = parsed_json.get("title", "")
    # 获取所有节点信息
    sections = parsed_json.get("sections", [])
    flat_sections = flatten_sections(sections)

    # 提取所有路径用于 selectbox
    options = [item["path"] for item in flat_sections]

    # 显示 selectbox
    selected_option = st.selectbox("选择一个部分查看详情", options)

    images = st.checkbox("是否需要图片", True)

    min_length = st.slider("最小字数", 200, 2000, value=600, step=100)

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

    # 添加按钮，点击后显示完整信息
    if st.button("获取当前节点的完整信息并生成内容"):
        if selected_section:
            # 获取当前节点及子节点信息
            current_section_info = get_subsections_info(selected_section)

            # 获取父节点链信息
            parent_chain = get_parent_chain(flat_sections, selected_option)

            # 展示父节点链信息
            # 现阶段只是展示章信息所以不需要展示父节点信息，联动注释见方法flatten_sections
            # st.markdown("### 父节点链信息：")
            # for parent in parent_chain:
            #     st.markdown(f"- **{parent['title']}**: {parent['abstract']}")

            # 展示子节点链信息
            st.markdown("### 子节点链信息：")

            sub_nodes = []
            display_section_info(current_section_info, sub_nodes)

            # 获取所有叶子节点，为以后生产内容做准备

            for sub_node in sub_nodes:
                logger.info(sub_node)

            with st.spinner("AI正在思考中，请稍等..."):
                response = app.invoke(
                    input={
                        "project_name": project_name,
                        "summarizations": st.session_state["summarizations"],
                        "outline": st.session_state["outline"],
                        "todo_list": sub_nodes,
                        "done_list": [],
                        "images": images,
                        "min_length": min_length,
                    },
                    config={
                        "recursion_limit": 64,
                        "configurable": {"llm": "anthropic"},
                    },
                )

            with open(response["article_path"], "rb") as file:
                file_bytes = file.read()

                # 获取当前时间戳
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                st.download_button(
                    label="文件下载",
                    data=file_bytes,
                    file_name=f"tender_document_{timestamp}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )

        else:
            st.error("未选中任何节点！")
