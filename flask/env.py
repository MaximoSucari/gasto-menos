import os
import openai
from dotenv import load_dotenv

# OPENAI
_ = load_dotenv(".env")
openai.api_key = os.environ["OPENAI_API_KEY"]

# CHROMA
PERSIST_DIRECTORY = "CategoriesDB"

def change_sqlite_settings():
    __import__("pysqlite3")
    import sys

    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")


change_sqlite_settings()


