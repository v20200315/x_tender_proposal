from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

template = """
你是一位专业的写作助手，擅长从复杂文档中提炼清晰且准确的总结。你的任务是根据提供的文档列表，撰写一段约500字的总结。这段总结需要：  

1. 清晰阐述文档列表的主要内容、主题和目的。  
2. 突出文档中包含的重要细节、关键数据或结论。  
3. 使用正式且信息丰富的语言风格，适合专业或学术场景。  
4. 确保总结是自成一体的，即使读者未阅读原始文档，也能理解其内容。  

总结撰写步骤如下：  
- 提取每个文档的核心主题或目的。  
- 找出关键点，包括背景、发现或结论。  
- 将内容组织得有逻辑性，确保段落之间流畅衔接。  

例如，如果文档是技术方案，描述其目标、方法和预期成果；如果是研究报告，强调其范围、主要发现及影响。  

最后，确保输出的总结结构清晰、语言流畅，适合正式场合使用。  

以下是需要总结的文本列表：
{documents}

"""

prompt = PromptTemplate(input_variables=["documents"], template=template)


summarize_docs_chain = prompt | llm | StrOutputParser()
