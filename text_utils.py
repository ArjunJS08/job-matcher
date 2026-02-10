from pypdf import PdfReader
from docx import Document

def extract_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return " ".join(p.extract_text() for p in reader.pages if p.extract_text())

    if file_path.endswith(".docx"):
        doc = Document(file_path)
        return " ".join(p.text for p in doc.paragraphs)

    if file_path.endswith(".txt"):
        return open(file_path, encoding="utf-8").read()

    return ""
