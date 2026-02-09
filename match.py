import chromadb
from chromadb.config import Settings
from config import CHROMA_DIR

client = chromadb.Client(
    Settings(persist_directory=CHROMA_DIR)
)

resumes = client.get_collection("resumes")
jobs = client.get_collection("jobs")

def match_job(job_id):
    job = jobs.get(ids=[job_id])
    job_embed = job["embeddings"][0]
    job_meta = job["metadatas"][0]

    results = resumes.query(
        query_embeddings=[job_embed],
        n_results=50
    )

    final = []
    for i in range(len(results["ids"][0])):
        meta = results["metadatas"][0][i]
        score = results["distances"][0][i]

        if meta["location"] == job_meta["location"]:
            final.append((results["ids"][0][i], round(1 - score, 3)))

    return sorted(final, key=lambda x: x[1], reverse=True)[:10]
