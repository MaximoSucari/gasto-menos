import os
import env
from env import PERSIST_DIRECTORY
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document

categories = [
    "Restaurantes y bares",
    "Compras",
    "Cultura",
    "Deporte",
    "Educación",
    "Salud",
    "Servicios",
    "Transporte",
    "Turismo",
]


def create_db():
    documents = [
        Document(page_content=category, metadata={}) for category in categories
    ]
    embedding = OpenAIEmbeddings()
    if os.path.exists(PERSIST_DIRECTORY):
        smalldb = Chroma(
            persist_directory=PERSIST_DIRECTORY, embedding_function=embedding
        )
        print("Chroma already exists on disk.")
    else:
        smalldb = Chroma.from_documents(
            documents=documents,
            embedding=embedding,
            persist_directory=PERSIST_DIRECTORY,
        )
