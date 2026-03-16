import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN not found. Please add it to your .env file")

# Initialize OpenAI client (via Hugging Face router)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)

# Load embeddings and vectorstore
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# --- Streamlit UI ---
st.set_page_config(page_title="RAG Assistant", page_icon="🤖")

st.title("📚 RAG-powered Assistant")
st.write("Ask questions and get answers based on your FAISS vectorstore context.")

# Input box
query = st.text_input("Enter your question:")

if query:
    # Retrieve relevant docs
    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])

    # Build prompt
    prompt = f"""
    You are a helpful assistant.

    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {query}
    """

    # Call LLM
    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = completion.choices[0].message.content

    # Display results
    st.subheader("Answer")
    st.write(answer)

    with st.expander("Retrieved Context"):
        st.write(context)