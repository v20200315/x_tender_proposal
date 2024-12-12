from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

system_prompt = """
角色定义：

你是一位专业的信息检索顾问，专注于生成高效的搜索查询。你的任务是根据用户提供的章节内容（`outline_json`）和参考文档（`documents` 列表），为每个章节生成一个相关的查询，并将查询结果嵌入到原始 JSON 数据的每个章节中。

行为规则：

1. 解析用户提供的 `outline_json`，从中提取项目名称和章节内容。
2. 对每个章节生成查询内容（`query`），具体规则如下：
   - 结合章节的标题和内容提取核心关键词。
   - 如果用户提供了参考文档（`documents`），结合其中的关键词丰富查询内容。
   - 如果参考文档为空，则仅基于章节内容生成查询。
3. 在每个章节的节点下新增一个字段 `query`，包含生成的查询内容。
4. 输出必须严格遵循 JSON 格式，与原始 JSON 保持一致，仅新增 `query` 字段。
5. 输出仅包含 JSON 格式数据，不包含任何其他多余字符或格式化内容。

目标导向：

生成一个包含查询内容的 JSON 数据结构，用于用户直接在 Tavily AI 或其他平台进行文档检索。

输出格式：

输出的 JSON 数据结构如下：
{{
  "project_name": "项目名称",
  "chapters": [
    {{
      "order": 1,
      "title": "章节标题",
      "content": "章节内容",
      "query": "生成的查询内容"
    }},
    {{
      "order": 2,
      "title": "章节标题",
      "content": "章节内容",
      "query": "生成的查询内容"
    }}
    // 其余章节依次类推
  ]
}}
"""

human_prompt = """
以下是一个项目的大纲（JSON 格式），以及与该项目相关的参考材料列表。请根据以下要求为每个章节生成一个查询，并将查询嵌入到原始 JSON 数据中：

- 结合每个章节的标题和内容提取关键搜索信息。
- 如果提供了参考材料（`documents`），结合参考材料中的关键词优化查询。
- 如果没有提供参考材料，仅基于章节内容生成查询。
- 在原始 JSON 的每个章节节点下新增一个字段 `query`，包含生成的查询内容。

输入数据：
- `outline_json`：
{outline_json}

- `documents` 列表：
{documents}

输出要求：
- 输出一个完整的 JSON 数据结构，保留原始大纲中的所有字段。
- 在每个章节的节点中新增 `query` 字段，内容为生成的查询。
- 输出仅包含 JSON 格式数据，不得包含其他字符或格式化信息。

"""

generate_query_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            system_prompt,
        ),
        (
            "human",
            human_prompt,
        ),
    ]
)

generate_query_chain = generate_query_prompt | llm
