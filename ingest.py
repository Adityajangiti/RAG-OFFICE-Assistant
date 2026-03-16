import os

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

data_path = "data"

documents = []

for file in os.listdir(data_path):

    path = os.path.join(data_path, file)

    if file.endswith(".pdf"):
        loader = PyPDFLoader(path)
        documents.extend(loader.load())

    elif file.endswith(".docx"):
        loader = Docx2txtLoader(path)
        documents.extend(loader.load())


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)

# Use HuggingFace Embeddings instead of OpenAI
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(docs, embeddings)

vectorstore.save_local("vectorstore")

print("Documents embedded successfully")