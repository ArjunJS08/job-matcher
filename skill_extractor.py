import json
from llm import extract_skills

def parse_skills(text):
    result = extract_skills(text)
    data = json.loads(result)
    return data["primary"], data["secondary"]
