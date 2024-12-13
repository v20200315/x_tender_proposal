import os
import streamlit as st
from x_outline.graph.graph import app

st.set_page_config(page_title="投标文件生成器")
st.markdown("#### 投标文件Outline生成器")
st.markdown("###### Special for: 软件项目技术方案建议书")
uploaded_file = st.file_uploader(
    "暂时只支持上传一个PDF格式的文件", type="pdf", accept_multiple_files=False
)

# 定义存放文件的目录
output_dir = "temp"
os.makedirs(output_dir, exist_ok=True)  # 创建目录，如果已存在则不会报错

button = st.button("生成", disabled=not uploaded_file)
if uploaded_file and button:
    with st.spinner("AI正在思考中，请稍等..."):
        file_content = uploaded_file.read()
        temp_file_path = os.path.join(output_dir, "temp.pdf")
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(file_content)
        result = app.invoke(input={"paths": [temp_file_path]})
        st.text_area(
            "Outline",
            result["outline"],
            height=500,
        )
    # try:
    #     with st.spinner("AI正在思考中，请稍等..."):
    #         file_content = uploaded_file.read()
    #         temp_file_path = os.path.join(output_dir, "temp.pdf")
    #         with open(temp_file_path, "wb") as temp_file:
    #             temp_file.write(file_content)
    #         result = app.invoke(input={"paths": [temp_file_path]})
    #         st.text_area(
    #             "Outline",
    #             result["outline"],
    #             height=500,
    #         )
    # except Exception as e:
    #     st.error("此服务暂时只支持软件项目技术方案建议书。")
