import chromadb
from chromadb.config import Settings
from embedder import embed
from skill_extractor import parse_skills
from config import CHROMA_DIR
import os, uuid

client = chromadb.Client(
    Settings(persist_directory=CHROMA_DIR)
)

resume_col = client.get_or_create_collection("resumes")
job_col = client.get_or_create_collection("jobs")

def ingest_resumes(path="data/resumes"):
    for file in os.listdir(path):
        text = open(f"{path}/{file}", encoding="utf8").read()
        primary, secondary = parse_skills(text)

        resume_col.add(
            ids=[str(uuid.uuid4())],
            documents=[text],
            embeddings=[embed(text)],
            metadatas=[{
                "primary_skills": primary,
                "secondary_skills": secondary,
                "experience": 5,
                "location": "Bangalore",
                "role": "Backend"
            }]
        )

    client.persist()

def ingest_jobs(path="data/jobs"):
    for file in os.listdir(path):
        text = open(f"{path}/{file}", encoding="utf8").read()

        job_col.add(
            ids=[file],
            documents=[text],
            embeddings=[embed(text)],
            metadatas=[{
                "min_exp": 3,
                "max_exp": 8,
                "location": "Bangalore",
                "role": "Backend"
            }]
        )

    client.persist()
