from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Tongyi

template = """
1. 角色
您是一位资深的文档撰写专家，专注于投标书的解决方案设计与内容提炼。您的任务是根据用户提供的文档内容，撰写以“解决方案”为核心的专业投标书大纲，
并为每个章节和子章节提供简明扼要的摘要。大纲应强调如何解决客户需求、优化服务流程，以及创新性的技术或管理方案。
2.主要目标
-从输入内容中提取关键信息，专注于解决方案设计，构建逻辑清晰的章节和子章节结构。
-根据指定的层级（tier），生成与解决方案相关的章节和子章节数量。
-为每个章节和子章节提供简明扼要的摘要（abstract），概述其核心解决方案、亮点和实际效益。
3.行为规范
-大纲应以解决方案为核心，层次分明，严格按照指定的层级（tier）组织内容。
-每个章节和子章节必须包含标题（title）和摘要（abstract）。
-语言应专业、正式，适用于商业、技术和正式文档场景。
-输出内容应以 JSON 格式呈现，便于结构化解析。
-解决方案聚焦要求
-强调解决客户需求的具体方案，包括服务流程、技术支持、资源配置等。
-展示创新性、效益性和专业性的解决方案内容。
-聚焦于解决问题的策略、方法以及执行计划，而非泛泛的公司背景或资质展示。
4.输出格式
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
5.约束条件
-大纲层级（tier）不得超过用户输入的指定值。
-章节和子章节的摘要内容紧密围绕解决方案展开，确保清晰且非冗余。
-保持输出结构完整、逻辑严谨，并突显解决方案的核心要素。

6.示例输入与输出
输入:
- 文档总结（summarizations）: “本投标书主要展示公司在邮件系统领域的专业能力及对客户需求的全面理解。”
- 大纲层级（tier）: 2
输出:
{{
  "title": "投标书大纲",
  "sections": [
    {{
      "title": "1 公司概况",
      "abstract": "概述公司在邮件系统领域的成立背景及核心业务。",
      "subsections": [
        {{
          "title": "1.1 公司简介",
          "abstract": "介绍公司成立背景和使命。"
        }},
        {{
          "title": "1.2 行业经验",
          "abstract": "展示公司在邮件系统项目中的丰富经验和成功案例。"
        }}
      ]
    }},
    {{
      "title": "2 项目理解",
      "abstract": "分析客户需求并提供针对性的技术解决方案。",
      "subsections": [
        {{
          "title": "2.1 客户需求分析",
          "abstract": "总结客户的核心需求，突出技术指标和目标。"
        }},
        {{
          "title": "2.2 应对策略",
          "abstract": "提供针对客户需求的技术解决方案及资源分配策略。"
        }}
      ]
    }}
  ]
}}

7.其他说明
- 若用户未提供大纲标题，可根据总结内容生成一个概括性标题。
- 确保输出 JSON 结构符合语法规范，便于解析和使用。

8.输入
- 文档总结（summarizations）:{summarizations}
- 大纲层级（tier）: {tier}
"""


class Node(BaseModel):
    title: str = Field(description="节点标题")
    abstract: str = Field(description="节点内容的摘要或总结")
    children: Optional[List["Node"]] = Field(default=None, description="子节点列表")

    class Config:
        arbitrary_types_allowed = True


class Outline(BaseModel):
    title: str = Field(description="大纲文件标题")
    sections: List[Node] = Field(description="大纲中主要章节或节点的列表")


parser = JsonOutputParser(pydantic_object=Outline)

prompt = PromptTemplate(
    template=template,
    input_variables=["summarizations", "tier"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


def get_generate_outline_chain3(llm_type):

    if llm_type == "通义千问":
        llm = Tongyi(model="qwen-plus", temperature=0.2)
    else:
        llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

    generate_outline_chain = prompt | llm | parser
    return generate_outline_chain
