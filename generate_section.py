import os
from datetime import datetime
import streamlit as st
from x_section.graph.graph import app

st.set_page_config(page_title="投标文件生成器")
st.markdown("#### 投标文件章节内容生成器")
st.markdown("###### Special for: 软件项目技术方案建议书")

# 初始化状态
if "button_enabled" not in st.session_state:
    st.session_state["button_enabled"] = True
if "processing" not in st.session_state:
    st.session_state["processing"] = False


uploaded_file = st.file_uploader(
    label="相关文档（暂时只支持上传一个PDF格式的文件）",
    type="pdf",
    accept_multiple_files=False,
)

project_name = st.text_input("项目名称")
min_length = st.number_input("最小字数", min_value=200, step=1000)
section1 = st.text_input("章节1")
section2 = st.text_input("章节2")
section3 = st.text_input("章节3")
section4 = st.text_input("章节4")
section5 = st.text_input("章节5")


def handle_click():
    st.session_state["button_enabled"] = False
    st.session_state["processing"] = True


# 按钮逻辑
button_clicked = st.button(
    "生成",
    disabled=not st.session_state["button_enabled"],
    on_click=handle_click,
)


# 执行业务逻辑
if st.session_state.processing:
    st.session_state["button_enabled"] = True
    st.session_state["processing"] = False

    if not uploaded_file:
        st.info("请上传相关文档，用于生成更加完整合理的信息。")
        st.stop()

    if not project_name:
        st.info("请输入项目名称。")
        st.stop()

    if not section1:
        st.info("请输入章节内容。")
        st.stop()

    # 定义存放文件的目录
    output_dir = "temp"
    os.makedirs(output_dir, exist_ok=True)  # 创建目录，如果已存在则不会报错

    with st.spinner("AI正在思考中，请稍等..."):
        file_content = uploaded_file.read()
        temp_file_path = os.path.join(output_dir, "temp.pdf")
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(file_content)

        input_texts = []

        for section in [section1, section2, section3, section4, section5]:
            if section:
                input_texts.append(section)

        result = app.invoke(
            input={
                "paths": [temp_file_path],
                "project_name": project_name,
                "min_length": min_length,
                "input_texts": input_texts,
            }
        )

    with open(result["section_path"], "rb") as file:
        file_bytes = file.read()

        # 获取当前时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        st.download_button(
            label="文件下载",
            data=file_bytes,
            file_name=f"tender_section_{timestamp}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
