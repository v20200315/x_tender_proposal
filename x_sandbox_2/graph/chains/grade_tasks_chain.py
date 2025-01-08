from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

grade_tasks_template = """
你是一位专业的任务分类分析师，擅长判断任务是否属于投标文件大纲的调整与优化任务。以下是用户提供的任务描述：  

\\n\\n任务描述 (task)：{task}  

\\n\\n请根据以下要求进行判断：  

1. 阅读任务描述，判断其是否涉及对投标文件大纲的结构调整或内容优化。  
2. 如果任务与投标文件大纲调整优化相关（如调整大纲结构、优化内容细节等），返回 “yes”。  
3. 如果任务与投标文件大纲调整优化无关，返回 “no”。  
4. 输出必须为小写的 “yes” 或 “no”，不包含任何其他内容。  

\\n\\n输出格式：\\n\\n  
yes  
或  
no
"""

grade_tasks_prompt = ChatPromptTemplate(
    [("human", grade_tasks_template)]
)

grade_tasks_chain = grade_tasks_prompt | llm | StrOutputParser()
