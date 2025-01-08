from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# llm = ChatTongyi(model="qwen-max", temperature=0)

map_template = """
简要概括以下内容:\\n\\n{content}
"""
map_prompt = ChatPromptTemplate([("human", map_template)])

map_chain = map_prompt | llm | StrOutputParser()
