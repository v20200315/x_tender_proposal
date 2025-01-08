from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from x_sandbox.graph.tools import Outline

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# llm = ChatTongyi(model="qwen-max", temperature=0)

generate_outline_template = """
你是一位专业的标书策划专家，擅长根据招标文件的需求设计结构清晰、内容完整的大纲。
以下是用户提供的内容摘要,需求列表,招标分类，请为解决方案部分生成对应的招标文件大纲，突出该分类的核心内容和特点。
\\n\\n输入内容：\\n\\n
内容摘要（final_summarization）：{final_summarization}
需求列表（requirements）：{requirements}
招标分类（classification）：{classification}
\\n\\n输出要求：\\n\\n
生成一份围绕解决方案部分的招标文件大纲，按三层结构组织（如：第一章 -> 1.1 节 -> 1.1.1 小节）。
大纲需结合分类特点，确保逻辑清晰，内容全面，包括但不限于以下方面：
项目概述与目标
技术方案或服务设计
实施计划与保障措施
每一章节需突出核心重点，体现对分类特点的深刻理解。
为每个章节和子章节提供一段简明扼要的摘要（abstract），概述其内容和重点信息。
\\n\\n生成规则：\\n\\n
第一章：概述部分，包含项目背景、需求与目标。
第二章：具体的解决方案设计，根据分类特点深入展开（如技术方案、服务内容等）。
第三章：实施与保障措施，展示执行能力和可持续性。

输出格式
JSON 格式的输出需符合以下结构：
{{
  "title": "{{大纲标题}}",
  "sections": [
    {{
      "title": "1 {{章节标题}}",
      "abstract": "{{摘要内容}}",
      "subsections": [
        {{
          "title": "1.1 {{子章节标题}}",
          "abstract": "{{摘要内容}}",
          "subsections": [
            {{
              "title": "1.2 {{子子章节标题}}",
              "abstract": "{{摘要内容}}"
            }}
          ]
        }}
      ]
    }}
  ]
}}
"""

generate_outline_prompt = ChatPromptTemplate([("human", generate_outline_template)])

generate_outline_chain = (
        generate_outline_prompt | llm | JsonOutputParser(pydantic_object=Outline)
)
