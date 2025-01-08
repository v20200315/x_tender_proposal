import asyncio
import json
import os
import streamlit as st

from x_sandbox.graph.graph import app

st.set_page_config(page_title="沙箱步骤一")

uploaded_file = st.file_uploader(
    "相关文档（暂时只支持上传一个PDF格式的文件）",
    type="pdf",
    accept_multiple_files=False,
)

submit = st.button("开始生成Outline")

if submit:
    # 定义存放文件的目录
    output_dir = "temp"
    os.makedirs(output_dir, exist_ok=True)  # 创建目录，如果已存在则不会报错

    with st.spinner("AI正在思考中，请稍等..."):
        file_content = uploaded_file.read()
        temp_file_path = os.path.join(output_dir, "temp.pdf")
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(file_content)

        async def process():
            return await app.ainvoke(
                {"paths": [temp_file_path]},
                {"recursion_limit": 128},
            )

        response = asyncio.run(process())
        st.session_state["response_1"] = response
        with st.container(height=500):
            st.write("Outline")
            formatted_json = json.dumps(
                response["outline"], indent=4, ensure_ascii=False
            )
            st.code(formatted_json, wrap_lines=True, language="json")

        st.page_link("sandbox2.py", label="确认Outline", icon="☕")
