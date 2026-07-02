import json
from pathlib import Path

from sqlalchemy.orm import Session

from backend.database.models import Document
from backend.repositories.document_repository import DocumentRepository
from backend.repositories.writing_profile_repository import (
    WritingProfileRepository
)
from backend.services.document_parser import extract_text
from backend.services.groq_style_analyzer import analyze_style_with_groq


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DOCUMENTS_DIR = BASE_DIR / "uploads" / "documents"
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)


def process_document(
    file_name: str,
    file_bytes: bytes,
    db: Session,
    user_id: int
):
    # Save uploaded file
    extension = Path(file_name).suffix
    file_path = DOCUMENTS_DIR / f"writing_reference{extension}"

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    # Extract text
    text = extract_text(str(file_path))

    # Save document to PostgreSQL
    document = Document(
        user_id=user_id,
        filename=file_name,
        file_path=str(file_path),
        extracted_text=text
    )

    DocumentRepository.create(
        db=db,
        document=document
    )

    # Analyze writing style
    profile = analyze_style_with_groq(text)

    profile = profile.replace("```json", "")
    profile = profile.replace("```", "")
    profile = profile.strip()

    profile = json.loads(profile)

    

    WritingProfileRepository.create(
    db=db,
    user_id=user_id,
    profile=profile
)

    return {
    "success": True,
    "message": "Document uploaded successfully.",
    "profile_created": True
}