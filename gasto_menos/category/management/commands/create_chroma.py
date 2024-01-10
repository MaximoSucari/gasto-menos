from django.conf import settings
from category.models import Category
from django.core.management.base import BaseCommand

import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document


class Command(BaseCommand):
    help = "Create a category database for nlp"

    def handle(self, *args, **options):
        documents = []

        for category in Category.objects.all():
            content = category.name + " " + category.keywords
            documents.append(
                Document(page_content=content, metadata={"category": category.name})
            )

        embedding = OpenAIEmbeddings()
        if os.path.exists(settings.CHROMA_PERSIST_DIR):
            smalldb = Chroma(
                persist_directory=settings.CHROMA_PERSIST_DIR,
                embedding_function=embedding,
            )
            print("Chroma already exists on disk.")
        else:
            smalldb = Chroma.from_documents(
                documents=documents,
                embedding=embedding,
                persist_directory=settings.CHROMA_PERSIST_DIR,
            )
