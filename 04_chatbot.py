from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def chat():
    messages = [
        {"role": "system", "content": "You are a helpful, concise assistant. Keep answers under 4 sentences unless asked for detail."}
    ]
    
    print("Chatbot ready (qwen3.5:4b, local). Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye.")
            break
        if not user_input:
            continue
        
        messages.append({"role": "user", "content": user_input})
        
        print("🤖: ", end="", flush=True)
        full_response = ""
        
        stream = client.chat.completions.create(
            model="qwen3.5:4b",
            extra_body={"options": {"num_gpu": 99}},  # Try to offload as many layers as possible
            messages=messages,
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                print(token, end="", flush=True)
                full_response += token
        
        print()
        messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    chat()