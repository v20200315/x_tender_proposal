from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

from x_sandbox_2.graph.tools import Outline

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

adjust_outline_structure_template = """
你是一位专业的大纲优化专家，擅长根据用户提供的任务对大纲的结构进行调整。以下是用户的输入：  

\\n\\n任务描述 (task)：{task}  
大纲 (outline)：{outline}  

\\n\\n请根据以下要求调整大纲结构：  

1. 阅读任务描述 (task)，理解任务对大纲结构调整的具体需求。  
2. 根据任务要求，仅对大纲的章节顺序、层级结构、标题设置等进行相应调整，禁止修改任何内容的具体细节。  
3. 保留大纲的逻辑性与清晰性，确保调整后每一章、节、子节的结构明确且无歧义。  
4. 如果任务未明确具体调整方式，请结合常规优化逻辑进行合理的结构调整。  
5. 输出的调整结果应仅体现大纲结构的变动，内容部分保持完全不变。  

\\n\\n输出格式：\\n\\n  
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

adjust_outline_structure_prompt = ChatPromptTemplate(
    [("human", adjust_outline_structure_template)]
)

adjust_outline_structure_chain = (
        adjust_outline_structure_prompt | llm | JsonOutputParser(pydantic_object=Outline)
)
