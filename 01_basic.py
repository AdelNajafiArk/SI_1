from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # required but ignored
)

response = client.chat.completions.create(
    model="qwen3.5:4b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain what an AI Engineer does in 3 sentences."}
    ]
)

print(response.choices[0].message.content)
print(f"\nTokens: {response.usage.total_tokens if response.usage else 'N/A'}")