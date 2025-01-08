from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=1)

review_outline_template = """
根据用户提供的摘要(final_summarization)


你是一位专业的标书策划专家，擅长审阅和优化针对解决方案部分的标书大纲。以下是用户提供的上下文内容 (contents) 和初步生成的大纲 (outline) ，
请根据以下要求对大纲进行审核和优化：
\\n\\n输入内容：\\n\\n
上下文内容（contents）：{contents}
初步大纲(outline)：{outline}
\\n\\n优化要求：\\n\\n
1. 如果上下文内容 (contents) 涉及解决方案部分，提取其中的关键信息，并将其融入大纲。
2. 保留大纲的三层结构（如：第一章 -> 1.1 节 -> 1.1.1 小节），同时增强其逻辑性与针对性（最多三层，不许超过三层）。
3. 确保优化后的大纲能突出解决方案的核心要点，包括但不限于以下方面：
-项目背景与需求
-技术或服务方案的核心设计
-实施计划与保障措施
4. 如果发现初步大纲与上下文内容不完全匹配，请进行调整或补充以确保一致性。
\\n\\n生成规则：\\n\\n
第一章：概述项目背景与需求，确保清晰传达项目整体目标。
第二章：详细描述解决方案部分，针对上下文内容中的具体技术或服务要求。
第三章：规划实施与保障，强调投标人的执行能力和创新性。
"""

review_outline_prompt = ChatPromptTemplate([("human", review_outline_template)])

review_outline_chain = review_outline_prompt | llm | StrOutputParser()
