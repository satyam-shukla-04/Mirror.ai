from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.api.dependecies.auth import get_current_user
from backend.database.models.user import User

from backend.repositories.document_repository import DocumentRepository
from backend.repositories.generated_text_repository import GeneratedTextRepository
from backend.repositories.generated_voice_repository import GeneratedVoiceRepository
from backend.repositories.profile_repositories import ProfileRepository

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    documents = DocumentRepository.get_all(
        db=db,
        user_id=current_user.id,
    )

    texts = GeneratedTextRepository.get_all(
        db=db,
        user_id=current_user.id,
    )

    voices = GeneratedVoiceRepository.get_all(
        db=db,
        user_id=current_user.id,
    )

    writing_ready = False
    voice_ready = False

    try:
        ProfileRepository.get_style_profile(
            db,
            current_user.id,
        )
        writing_ready = True
    except:
        pass

    try:
        ProfileRepository.get_voice_profile(
            db,
            current_user.id,
        )
        voice_ready = True
    except:
        pass

    return {
        "documents": len(documents),
        "generated_texts": len(texts),
        "generated_voices": len(voices),
        "writing_profile": writing_ready,
        "voice_profile": voice_ready,
    }