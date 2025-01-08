from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import ListOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

parse_feedback_template = """
你是一位专业的任务分析师，擅长从用户提供的反馈 (feedback) 中提取具体的行动事项。以下是用户的反馈内容：  

\\n\\n用户反馈 (feedback)：{feedback}  

\\n\\n请根据以下要求提取用户需要完成的事项：  

1. 阅读用户反馈，分析反馈中明确提到的任务或需求。  
2. 如果反馈中包含隐含的任务或未明确表达的需求，结合上下文推导出这些任务。  
3. 如果反馈中没有明确的任务或需求，返回空字符串，不输出任何内容。  
4. 确保任务描述清晰、具体，可直接执行。  
5. 仅输出任务描述，每个任务单独占一行，不添加编号或无关内容。  

\\n\\n输出格式：\\n\\n  
任务描述 1  
任务描述 2  
任务描述 3  
...  

注意：  
- 任务描述应直接来源于用户反馈，不得添加无关内容。  
- 如果无法从反馈中明确提取任务或需求，直接返回空字符串。    
"""


class TaskListOutputParser(ListOutputParser):
    def parse(self, text: str) -> list:
        # 假设返回值是通过换行分割的列表
        if text.strip():
            return text.strip().split("\n")
        else:
            return []


parse_feedback_prompt = ChatPromptTemplate([("human", parse_feedback_template)])

parse_feedback_chain = parse_feedback_prompt | llm | TaskListOutputParser()
