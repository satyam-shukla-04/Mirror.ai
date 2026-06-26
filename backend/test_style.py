from pathlib import Path
from services.style_analyzer import analyze_style
from services.groq_style_analyzer import analyze_style_with_groq
BASE_DIR = Path(__file__).resolve().parent.parent

file_path = (
    BASE_DIR
    / "data"
    / "extracted_text"
    / "NEW HALL-TICKET.txt"
)

print("Reading:", file_path)

with open(
    file_path,
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

profile = analyze_style_with_groq(text)
print(profile)