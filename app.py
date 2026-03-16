import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    HF_TOKEN = os.getenv("HF_TOKEN")
)

completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "user", "content": "Create a recipe for a chocolate cake."}
    ]
)

print(completion.choices[0].message.content)