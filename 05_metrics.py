import time
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def measure(prompt):
    start = time.time()
    
    response = client.chat.completions.create(
        model="qwen3.5:4b",
        messages=[{"role": "user", "content": prompt}],
        extra_body={"options": {"num_gpu": 99}}  # Try to offload as many layers as possible
    )
    
    elapsed = time.time() - start
    content = response.choices[0].message.content
    
    # Count words as rough token proxy
    token_estimate = len(content.split()) * 1.3
    
    print(f"Prompt: {prompt[:50]}...")
    print(f"Response length: {len(content)} chars")
    print(f"Est. tokens: {token_estimate:.0f}")
    print(f"Latency: {elapsed:.2f}s")
    print(f"Speed: {token_estimate/elapsed:.1f} tok/s\n")

measure("Explain machine learning in 2 sentences.")
#measure("Write a 10-word story about a robot.")