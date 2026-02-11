import os
from chroma_client import client
from embedder import embed
from skill_extractor import parse_skills
from text_utils import extract_text

resume_col = client.get_or_create_collection("resumes")
job_col = client.get_or_create_collection("jobs")


def ingest_resumes(path="data/resumes"):
    print(f"Scanning resumes folder: {os.path.abspath(path)}")
    files = os.listdir(path)
    print("Files:", files)

    added = 0

    for file in files:
        if not file.lower().endswith(".pdf"):
            continue

        text = extract_text(os.path.join(path, file))

        if not text or len(text.strip()) < 50:
            print(f"⚠️ Skipping {file}: no readable text (likely scanned PDF)")
            continue

        primary_skills, secondary_skills = parse_skills(text)

        resume_col.add(
            ids=[file],
            documents=[text],
            embeddings=[embed(text)],
            metadatas=[{
                "filename": file,
                "primary_skills": ", ".join(primary_skills),
                "secondary_skills": ", ".join(secondary_skills)
            }]
        )



        added += 1

    print(f"✅ Resumes added: {added}")


def ingest_jobs(path="data/jobs"):
    print(f"Scanning jobs folder: {os.path.abspath(path)}")
    files = os.listdir(path)
    print("Files:", files)

    added = 0

    for file in files:
        if not file.lower().endswith(".txt"):
            continue

        with open(os.path.join(path, file), encoding="utf-8") as f:
            text = f.read()

        primary_skills, secondary_skills = parse_skills(text)

        job_col.add(
            ids=[file],
            documents=[text],
            embeddings=[embed(text)],
            metadatas=[{
                "job_id": file,
                "skills": ", ".join(primary_skills + secondary_skills),
                "min_exp": 3,
                "max_exp": 8,
                "location": "Bangalore",
                "role": "Backend"
            }]
        )


        added += 1

    print(f"✅ Jobs added: {added}")


if __name__ == "__main__":
    ingest_resumes()
    ingest_jobs()
