from typing import Any, Dict

from langchain_core.agents import AgentAction

from x_sandbox_2.graph.chains.oracle_chain import oracle_chain
from x_sandbox_2.graph.state import GraphState


def run_oracle(state: GraphState) -> Dict[str, Any]:
    # print("---RUN ORACLE (X_SANDBOX_2)---")
    # print(f'intermediate_steps: {state["intermediate_steps"]}')
    #
    # # 使用当前状态调用 oracle_chain。
    # out = oracle_chain.invoke(state)
    #
    # # 从 oracle_chain 的响应中提取工具名称及其参数。
    # tool_name = out.tool_calls[0]["name"]
    # tool_args = out.tool_calls[0]["args"]
    #
    # # 创建一个 AgentAction 对象，记录所使用的工具和提供的输入。
    # action_out = AgentAction(
    #     tool=tool_name,
    #     tool_input=tool_args,
    #     # 工具运行后稍后确定(To be determined)。
    #     log="TBD",
    # )
    #
    # # 返回具有更新的“intermediate_steps”的新状态。
    # return {"intermediate_steps": [action_out]}
    return None
