from chroma_client import client

resume_col = client.get_collection("resumes")
job_col = client.get_collection("jobs")


def match_job(job_id: str, top_k: int = 10):
    job = job_col.get(ids=[job_id])

    if not job["documents"]:
        raise ValueError(f"Job {job_id} not found")

    job_text = job["documents"][0]
    job_meta = job["metadatas"][0]

    results = resume_col.query(
        query_texts=[job_text],
        n_results=top_k
    )

    print(f"\n🔍 Top {top_k} matches for Job: {job_id}\n")

    for i in range(len(results["ids"][0])):
        rid = results["ids"][0][i]
        score = 1 - results["distances"][0][i]  # cosine similarity
        meta = results["metadatas"][0][i]

        print(f"{i+1}. {meta['filename']}")
        print(f"   Score: {score:.3f}")
        print(f"   Primary skills: {meta['primary_skills']}")
        print(f"   Secondary skills: {meta['secondary_skills']}")
        print("-" * 50)


if __name__ == "__main__":
    match_job("job4.txt")
