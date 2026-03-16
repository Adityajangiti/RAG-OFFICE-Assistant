import langchain
langchain.debug = False
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


# Streamlit UI
st.set_page_config(page_title="RAG Assistant", page_icon="🤖")
st.title("📚 RAG Document Assistant")


# Initialize OpenAI client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)


# Load embeddings
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# Load vectorstore
@st.cache_resource
def load_vectorstore():
    embeddings = load_embeddings()
    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore


vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
query = st.chat_input("Ask a question about your documents...")


if query:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)


    # Retrieve documents
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


    # Generate response
    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = completion.choices[0].message.content


    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})