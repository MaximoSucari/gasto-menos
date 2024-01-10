import re
import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

from django.conf import settings

if os.path.exists(settings.CHROMA_PERSIST_DIR):
    embedding = OpenAIEmbeddings()
    smalldb = Chroma(
        persist_directory=settings.CHROMA_PERSIST_DIR, embedding_function=embedding
    )
else:
    print("WARNING: Chroma does not exist on disk.")


def get_category(text):
    results = smalldb.similarity_search(text, k=3)
    return results[0].metadata["category"]


def get_amount(text):
    pattern_k = r"(\d+\.?\d*)\s*k"
    pattern_usd = r"(\d+\.?\d*)\s*usd"

    match_k = re.search(pattern_k, text, re.IGNORECASE)
    match_usd = re.search(pattern_usd, text, re.IGNORECASE)

    if match_k:
        amount = float(match_k.group(1)) * 1000 if match_k.group(1) else 0.0
        currency = "pesos"
    elif match_usd:
        amount = float(match_usd.group(1)) if match_usd.group(1) else 0.0
        currency = "usd"
    else:
        return (0.0, "pesos")

    return (amount, currency)


def process_text(text):
    category = get_category(text)
    amount, currency = get_amount(text)

    return {"amount": amount, "currency": currency, "category": category}
