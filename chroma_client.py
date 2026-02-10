import chromadb
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db")

client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH
)

print("📁 Chroma persist directory:", CHROMA_DB_PATH)
