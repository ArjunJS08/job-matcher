import argparse
from ingest import ingest_resumes, ingest_jobs
from match import match_job

parser = argparse.ArgumentParser()

parser.add_argument("--ingest", choices=["resumes", "jobs"])
parser.add_argument("--match", help="Job ID")

args = parser.parse_args()

if args.ingest == "resumes":
    ingest_resumes()

elif args.ingest == "jobs":
    ingest_jobs()

elif args.match:
    matches = match_job(args.match)
    for r in matches:
        print(r)
