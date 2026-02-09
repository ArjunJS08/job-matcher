from openai import AzureOpenAI
from config import *

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def extract_resume_or_jd(text: str) -> dict:
    prompt = f"""
Extract structured information from the text below.

Return STRICT JSON with:
- primary_skills (max 8)
- secondary_skills (max 12)
- experience_years (integer)
- roles (normalized job roles)
- location
- remote_preference (true/false)
- relocation (true/false)

TEXT:
{text}
"""
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
