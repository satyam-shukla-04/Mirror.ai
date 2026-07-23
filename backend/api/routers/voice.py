from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.database.models.user import User
from backend.api.dependecies.auth import get_current_user
from backend.services.voice_upload_service import process_voice
from backend.services.voice_generation_service import generate_voice

from backend.api.schemas.voice_generate import (
    VoiceGenerateRequest,
    VoiceGenerateResponse,
)
from pathlib import Path

router = APIRouter(
    prefix="/voice",
    tags=["Voice"],
)


@router.post(
    "/generate",
    response_model=VoiceGenerateResponse,
)
def generate(
    request: VoiceGenerateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    voice = generate_voice(
        db=db,
        user_id=current_user.id,
        generated_text_id=request.generated_text_id
    )

    filename = Path(voice.audio_path).name

    return VoiceGenerateResponse(
    success=True,
    message="Voice generated successfully.",
    audio_path=f"/uploads/generated_voice/{filename}",
) 