import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

def decide_tool(user_input: str, tools_description: list) -> dict:
    tools_json = json.dumps(tools_description, ensure_ascii=False)

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "你是一个工具调度器。根据用户输入，判断需要调用哪个工具。\n"
                    f"可用工具：{tools_json}\n"
                    "只输出一个 JSON 对象，不要输出任何其他文字。\n"
                    "格式：{\"tool\": \"工具名或null\", \"args\": {\"参数名\": \"值\"}}\n"
                    "如果不需要调用工具，tool 设为 null，args 设为空对象。"
                ),
            },
            {"role": "user", "content": user_input},
        ],
        temperature=0,
    )

    raw = response.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"tool": None, "args": {}}


def chat_directly(user_input: str) -> str:
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": "你是一个有用的助手，直接回答用户问题。"},
            {"role": "user", "content": user_input},
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content