from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

examples = [
    {"task": "删除第一章", "output": "structure"},
    {"task": "删除第一章第二节", "output": "structure"},
    {"task": "去掉第二章第三节的2.3.1", "output": "structure"},
    {"task": "去掉第二章第三节的子层，并规划内容到第三节", "output": "structure"},
    {"task": "在第二章增加小节，名称为需求分析", "output": "structure"},
    {"task": "根据评分系统优化大纲", "output": "content"},
    {"task": "着重处理第三章内容", "output": "content"},
    {"task": "立足需求解决方案", "output": "content"},
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{task}"),
        ("ai", "{output}"),
    ]
)
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

classify_tasks_template = """
你是一位专业的大纲审阅分析师，擅长对任务进行分类，任务可能涉及大纲的结构调整 (structure) 或内容优化 (content)。以下是用户提供的任务描述：  

\\n\\n任务描述 (task)  

\\n\\n请根据以下规则对任务进行分类，并输出对应的分类名称：  

1. 如果任务与大纲章节顺序调整、层级变更、标题修改、格式统一等结构相关事项有关，则分类为 **结构调整 (structure)**。  
2. 如果任务与大纲中具体内容的扩展、补充、删减、细化描述等优化相关事项有关，则分类为 **内容优化 (content)**。  
3. 仅输出分类名称：**structure** 或 **content**，不包含其他任何内容。  

\\n\\n输出：\\n\\n  
structure  
或
content
"""

classify_tasks_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", classify_tasks_template),
        few_shot_prompt,
        ("human", "{task}"),
    ]
)

classify_tasks_chain = classify_tasks_prompt | llm | StrOutputParser()
