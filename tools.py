TOOL_REGISTRY = {}

def tool(name, description):
    def decorator(func):
        TOOL_REGISTRY[name] = {"func": func, "description": description}
        return func
    return decorator

'''
@tool("get_weather", "获取指定城市的天气，参数 city")
def get_weather(city: str) -> str:
    return f"{city} 今天晴，气温 22°C。"

@tool("calculator", "计算一个简单的数学表达式，参数 expression")
def calculator(expression: str) -> str:
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"计算失败：{e}"
'''