from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def ask(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="qwen3.5:4b",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

print("Q1:", ask("What is Python?"))
print("\nQ2:", ask("What did I just ask you?"))  # Tests memory