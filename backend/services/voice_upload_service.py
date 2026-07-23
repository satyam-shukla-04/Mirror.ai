from pathlib import Path
from sqlalchemy.orm import Session

from backend.repositories.voice_profile_repository import VoiceProfileRepository

BASE_DIR = Path(__file__).resolve().parent.parent.parent

VOICE_DIR = BASE_DIR / "uploads" / "voice_reference"
VOICE_DIR.mkdir(parents=True, exist_ok=True)


def process_voice(
    file_name: str,
    file_bytes: bytes,
    db: Session,
    user_id: int,
):

    extension = Path(file_name).suffix

    file_path = VOICE_DIR / f"voice_reference_{user_id}{extension}"

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    VoiceProfileRepository.create(
        db=db,
        user_id=user_id,
        audio_path=str(file_path),
    )

    return {
        "success": True,
        "message": "Voice uploaded successfully.",
        "voice_profile_created": True,
        "file_path": str(file_path),
    }