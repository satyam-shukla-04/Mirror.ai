from pathlib import Path
from document_parser import extract_text

BASE_DIR = Path(__file__).resolve().parent.parent.parent

file_path = BASE_DIR / "uploads" / "documents" / "NEW HALL-TICKET.pdf"

print(file_path)

text = extract_text(str(file_path))

print("Length:", len(text))
print(text[:500])