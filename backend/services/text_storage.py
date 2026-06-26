from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

EXTRACTED_DIR = BASE_DIR / "data" / "extracted_text"

EXTRACTED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def save_extracted_text(text):

    output_file = EXTRACTED_DIR / "writing_reference.txt"

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(text)

    return output_file