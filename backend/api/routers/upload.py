from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.services.upload_service import process_document
from backend.api.dependecies.auth import get_current_user
from backend.database.models.user import User
router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

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