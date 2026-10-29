from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session
from backend.services.voice_upload_service import process_voice
from backend.database.session import get_db
from backend.services.upload_service import process_document
from backend.services.voice_upload_service import process_voice
from backend.api.dependecies.auth import get_current_user
from backend.database.models.user import User
from backend.repositories.profile_repositories import ProfileRepository

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

# Upload document
@router.post("/document")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    file_bytes = await file.read()

    return process_document(
        file_name=file.filename,
        file_bytes=file_bytes,
        db=db,
        user_id=current_user.id
    )

# Upload voice
@router.post("/voice")
async def upload_voice(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    file_bytes = await file.read()

    return process_voice(
        file_name=file.filename,
        file_bytes=file_bytes,
        db=db,
        user_id=current_user.id
    )

@router.get("/voice/latest")
def latest_voice(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):

    voice = ProfileRepository.get_voice_profile(
        db=db,
        user_id=user.id,
    )

    if voice is None:
        raise HTTPException(
            status_code=404,
            detail="Voice profile not found."
        )

    return {
        "audio_path": voice.audio_path
    }