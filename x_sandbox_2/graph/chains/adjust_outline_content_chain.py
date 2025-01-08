from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_openai import ChatOpenAI

from x_sandbox_2.graph.tools import Outline

llm = ChatOpenAI(model="gpt-4o-mini", temperature=1)

adjust_outline_content_template = """
你是一位专业的标书策划专家，擅长分析任务需求并优化大纲。以下是用户提供的输入内容：  

\\n\\n输入内容：\\n\\n  
任务描述 (task)：{task}  
初步大纲 (outline)：{outline}  
需求列表 (requirements)：{requirements}  
内容摘要 (final_summarization)：{final_summarization}  

\\n\\n请根据以下要求调整并优化大纲：  

1. 阅读任务描述 (task)，理解其优化大纲的具体目标和方向。  
2. 分析需求列表 (requirements)和内容摘要 (final_summarization)，提取与任务描述相关的关键信息，并将其融入到大纲中。  
3. 保留大纲的三层结构（如：第一章 -> 1.1 节 -> 1.1.1 小节），确保逻辑清晰且内容精炼，不得超过三层。  
4. 优化后的大纲需突出以下核心要点：  
   - **项目背景与需求**：概述整体目标，提炼关键需求。  
   - **技术或服务方案的核心设计**：明确技术框架、服务流程和核心功能。  
   - **实施计划与保障措施**：规划执行方案，强化保障措施并提出创新策略。  
5. 如果任务描述 (task) 未明确具体要求，结合需求列表和内容摘要中的信息，对大纲进行合理调整和优化。  

\\n\\n生成规则：\\n\\n  
第一章：概述项目背景与需求，确保清晰传达项目整体目标。  
   - 每节需总结项目背景，并提炼需求列表中的核心需求点。  

第二章：详细描述解决方案部分，针对具体技术或服务要求。  
   - 每节需围绕内容摘要和需求列表展开，明确技术框架、服务流程及核心设计。  

第三章：规划实施与保障，强调投标人的执行能力和创新性。  
   - 每节需结合招标分类特点，规划执行计划、强化保障措施并提出创新策略。  

\\n\\n注意：  
- 调整后的大纲需结构合理，内容针对性强，与任务描述和需求高度一致。  
- 输出仅包括优化后的大纲，不添加额外解释或无关信息。  


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

adjust_outline_content_prompt = ChatPromptTemplate(
    [("human", adjust_outline_content_template)]
)

adjust_outline_content_chain = (
        adjust_outline_content_prompt | llm | JsonOutputParser(pydantic_object=Outline)
)
