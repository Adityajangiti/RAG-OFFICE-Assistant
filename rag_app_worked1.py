import os
from dotenv import load_dotenv
from openai import OpenAI

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# Load environment variables
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN not found. Please add it to your .env file")


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break


    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])


    prompt = f"""
You are a helpful assistant.

Use the context below to answer the question.

Context:
{context}

Question:
{query}
"""


    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )


    answer = completion.choices[0].message.content

    print("\nAnswer:\n", answer)