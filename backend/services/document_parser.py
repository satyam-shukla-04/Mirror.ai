from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_text(file_path: str):

    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return extract_pdf(file_path)

    elif suffix == ".docx":
        return extract_docx(file_path)

    elif suffix == ".txt":
        return extract_txt(file_path)

    else:
        return ""


def extract_pdf(file_path):

    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def extract_docx(file_path):

    doc = Document(file_path)

    return "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )


def extract_txt(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()