from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

print("🤖: ", end="", flush=True)

stream = client.chat.completions.create(
    model="qwen3.5:4b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short poem about debugging code."}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print()