from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_openai import ChatOpenAI

from x_sandbox_2.graph.tools import Outline

llm = ChatOpenAI(model="gpt-4o-mini", temperature=1)

# 输入参数是调整大纲结构的任务集(structure_tasks),调整大纲内容的任务集(content_tasks),初始的大纲(outline),大纲对应需求
# 集合(requirements)以及大纲对应文档的摘要(final_summarization).
# 任务是以大纲对应需求集合(requirements)和大纲对应文档的摘要(final_summarization)作为参考,完成调整大纲结构的任务集(structure_tasks)
# 和调整大纲内容的任务集(content_tasks)，这些所有的任务都是对初始的大纲(outline)调整优化的建议.
adjust_outline_template = """
你是一位专业的标书大纲优化专家，擅长根据任务集对大纲进行调整和优化。以下是用户提供的输入内容：  

\\n\\n输入内容：\\n\\n  
1. 调整大纲结构的任务集 (structure_tasks)：{structure_tasks}  
2. 调整大纲内容的任务集 (content_tasks)：{content_tasks}  
3. 初始大纲 (outline)：{outline}  
4. 大纲对应需求集合 (requirements)：{requirements}  
5. 大纲对应文档的摘要 (final_summarization)：{final_summarization}  

\\n\\n请根据以下要求完成对初始大纲的调整与优化：  

### 任务要求：  
1. **处理结构调整任务**：  
   - 阅读调整大纲结构的任务集 (structure_tasks)，理解每个任务的具体要求。  
   - 根据需求集合 (requirements) 和文档摘要 (final_summarization)，合理调整大纲的章节顺序、层级结构及标题设置。  
   - 确保调整后的大纲结构清晰、逻辑性强，且每一章节具有明确的内容指向。  

2. **处理内容优化任务**：  
   - 阅读调整大纲内容的任务集 (content_tasks)，分析任务对内容补充和优化的具体要求。  
   - 提取需求集合 (requirements) 和文档摘要 (final_summarization) 中的关键信息，将其融入到对应的大纲章节中。  
   - 优化内容时，确保用词精准，重点突出，并增强大纲的专业性和针对性。  

3. **确保大纲整体性与一致性**：  
   - 保留大纲的三层结构（如：第一章 -> 1.1 节 -> 1.1.1 小节），不得超过三层。  
   - 调整后的大纲需突出以下核心内容：  
     - 项目背景与需求：概述目标并提炼需求。  
     - 技术或服务方案的核心设计：展示设计逻辑与解决方案细节。  
     - 实施计划与保障措施：规划执行步骤，明确保障及创新策略。  

4. **任务执行顺序**：  
   - 先处理结构调整任务 (structure_tasks)，确保大纲框架合理。  
   - 再处理内容优化任务 (content_tasks)，增强大纲内容的完整性与针对性。  

\\n\\n输出规则：  
- 调整和优化后的完整大纲。  
- 大纲需体现所有任务集 (structure_tasks 和 content_tasks) 的调整要求，并结合需求集合 (requirements) 和文档摘要 (final_summarization)。  
- 不添加无关内容或多余解释，仅输出优化后的大纲结果。  

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

adjust_outline_prompt = ChatPromptTemplate(
    [("human", adjust_outline_template)]
)

adjust_outline_chain = (
        adjust_outline_prompt | llm | JsonOutputParser(pydantic_object=Outline)
)
