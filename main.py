from agent import SimpleAgent

def main():
    agent = SimpleAgent()
    print("hello! 我是vira，跟我聊聊天吧！")
    while True:
        user_input = input("input：").strip()
        if user_input.lower() in ("bye"):   # 输入bye退出
            break
        print(f"vira：{agent.run(user_input)}")

if __name__ == "__main__":
    main()