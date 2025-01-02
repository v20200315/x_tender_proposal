from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

classify_summarization_template = """
你是一位专业的分类识别专家，擅长根据文本内容精准判断其所属的类别。以下是用户提供的一段招标文件内容，请根据内容判断其所属的分类，
并直接输出分类名称。
分类包括以下类别：
建筑类，工程类，物业类，医疗类，物流类，广告类，IT类，园林类，市政类，保洁类，餐饮类，教育类，能源类，环保类，交通类，金融类，通讯类，
文化娱乐类，农业类，科研类，安全类
输入内容：
{final_summarization}
输出内容：
分类名称
"""

classify_summarization_prompt = ChatPromptTemplate([("human", classify_summarization_template)])

classify_summarization_chain = classify_summarization_prompt | llm | StrOutputParser()
