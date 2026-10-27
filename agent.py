from tools import TOOL_REGISTRY
from llm import decide_tool

class SimpleAgent:
    def __init__(self):
        self.tools = TOOL_REGISTRY

    def _build_tools_description(self):
        return [
            {"name": name, "description": info["description"]}
            for name, info in self.tools.items()
        ]

    def run(self, user_input: str) -> str:
        decision = decide_tool(user_input, self._build_tools_description())
        tool_name = decision.get("tool")
        args = decision.get("args", {})

        if not tool_name:
            from llm import chat_directly
            return chat_directly(user_input)

        if tool_name not in self.tools:
            return f"选择了未知工具：{tool_name}"

        func = self.tools[tool_name]["func"]
        try:
            return func(**args)
        except Exception as e:
            return f"工具执行出错：{e}"