from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# llm = ChatTongyi(model="qwen-max", temperature=0)

gather_requirements_template = """
你是一位专业的需求分析师，擅长从文档内容中提取核心需求信息及其细节。以下是用户提供的内容：  

\\n\\n内容 (content)：{content}  

\\n\\n请根据以下要求提取需求信息及其细节：  

1. 仔细阅读内容 (content)，定位与需求相关的描述，包括明确提及的需求和隐含的需求。  
2. 提取每项需求的核心信息，并在每项需求下列出其详细细节（如果有）。  
3. 确保提取的信息条理清晰、具体可操作，避免遗漏重要细节。  
4. 仅输出需求信息及其细节，以需求标题和其对应的细节内容分行展示。  

\\n\\n输出格式：\\n\\n  
需求 1：核心信息  
- 细节 1  
- 细节 2  
...  

需求 2：核心信息  
- 细节 1  
- 细节 2  
...  

注意：  
- 每项需求核心信息为一句简短总结，细节为对应的具体描述。  
- 如果内容中需求不明确，请基于描述合理推测需求。  

示例
输入内容：
招标文件中要求提供一套全生命周期的资产管理解决方案，包括资产的采购、使用、维护和报废管理，支持智能化监控和自动化流程，需具备良好的兼容性和可
扩展性。  
生成的输出：
需求 1：全生命周期资产管理解决方案  
- 涵盖资产的采购、使用、维护和报废管理  
- 支持智能化监控和自动化流程  

需求 2：解决方案的技术要求  
- 需具备良好的兼容性  
- 需具备良好的可扩展性  
"""

gather_requirements_prompt = ChatPromptTemplate(
    [("human", gather_requirements_template)]
)

gather_requirements_chain = gather_requirements_prompt | llm | StrOutputParser()
