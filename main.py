from src.agent import get_self_aware_agent


def main():
    print("Hello from memory-management!")
    agent = get_self_aware_agent()
    response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "What do you know about your local files"}
            ]
        }
    )
    print(response)


if __name__ == "__main__":
    main()
