from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

review_outline_template = """
你是一位专业的标书策划专家，擅长审阅和优化针对解决方案部分的标书大纲。以下是用户提供的上下文内容 (contents) 和初步生成的大纲 (outline) ，
请根据以下要求对大纲进行审核和优化：
\\n\\n输入内容：\\n\\n
上下文内容（contents）：{contents}
初步大纲(outline)：{outline}
\\n\\n优化要求：\\n\\n
1. 如果上下文内容 (contents) 涉及解决方案部分，提取其中的关键信息，并将其融入大纲。
2. 保留大纲的三层结构（如：第一章 -> 1.1 节 -> 1.1.1 小节），同时增强其逻辑性与针对性。
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
review_outline_template2 = """
#### 角色
您是一位资深的文档撰写专家，擅长投标书的结构化设计和内容提炼。您的任务是根据行业标准，为特定项目撰写专业的投标书大纲，
并为每个章节提供简明扼要的摘要。您将根据用户输入的文档内容进行总结，并依据指定的大纲层级，生成结构清晰的文档大纲。
#### 主要目标
1. 根据提供的内容（contents），review并优化给出的大纲（outline）。
2. 如果提供的内容中包含评分因素或者评审标准等段落内容，则大纲应该根据其内容指定，用以符合投标方的标准。
2. 如果提供的内容中未包含评分因素或者评审标准等段落内容，则根据技术规范等需求进行优化。
3. 大纲应该以中标为基本原则进行撰写，根据客户给出文档的喜好进行针对性的撰写，主要落实解决方案。
#### 输入
outline: {outline}
contents: {contents}
"""

review_outline_prompt = ChatPromptTemplate([("human", review_outline_template)])

review_outline_chain = review_outline_prompt | llm | StrOutputParser()
