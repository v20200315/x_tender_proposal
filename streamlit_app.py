from dotenv import load_dotenv
import streamlit as st

load_dotenv()

pages = {
    "控制台": [
        st.Page("home.py", title="主页", icon="🏠"),
        st.Page("dashboard.py", title="仪表盘", icon="📊"),
    ],
    "招标文件生成器": [
        st.Page("generate_outline.py", title="大纲生成器", icon="📋"),
        st.Page("generate_content.py", title="内容生成器", icon="📓"),
        st.Page("generate_section.py", title="章节内容生成器", icon="📓"),
    ],
    "招标文件生成器Pro": [
        st.Page("generate_outline_v2.py", title="大纲生成器Pro", icon="📋"),
        st.Page("generate_content_v2.py", title="内容生成器Pro", icon="📓"),
    ],
    "工具": [
        st.Page("cloned_chatgpt.py", title="克隆的ChatGPT", icon="💬"),
    ],
    "测试": [
        st.Page("human_feedback.py", title="Human Feedback", icon="💬"),
    ],
}

pg = st.navigation(pages)
pg.run()
