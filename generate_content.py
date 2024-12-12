import os
from time import sleep

import streamlit as st
from x_content.graph.graph import app

st.set_page_config(page_title="投标文件生成器")
st.markdown("#### 投标文件内容生成器")
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

input_text = st.text_area(
    label="输入Outline",
    height=300,
)


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

    if not input_text:
        st.info("请输入Outline，用于生成对应的文档。")
        st.stop()

    # 定义存放文件的目录
    output_dir = "temp"
    os.makedirs(output_dir, exist_ok=True)  # 创建目录，如果已存在则不会报错

    with st.spinner("AI正在思考中，请稍等..."):
        file_content = uploaded_file.read()
        temp_file_path = os.path.join(output_dir, "temp.pdf")
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(file_content)
        result = app.invoke(input={"paths": [temp_file_path], "input_text": input_text})

    with open(result["article_path"], "rb") as file:
        file_bytes = file.read()
        st.download_button(
            label="文件下载",
            data=file_bytes,
            file_name="tender_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

    # try:
    #
    # except Exception:
    #     st.error("请检查输入，如果无误请刷新页面再次尝试。或联系管理人员处理。")
