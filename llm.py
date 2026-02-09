from openai import AzureOpenAI
from config import *
AZURE_DEPLOYMENT = AZURE_OPENAI_DEPLOYMENT
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2024-02-01"
)

def extract_skills(text):
    prompt = f"""
    Extract:
    - Primary skills
    - Secondary skills
    Return JSON.
    Resume/JD:
    {text}
    """

    res = client.chat.completions.create(
        model=AZURE_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return res.choices[0].message.content
