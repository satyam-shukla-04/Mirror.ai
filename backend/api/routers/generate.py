from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.api.schemas.generate import (
    GenerateRequest,
    GenerateResponse
)
from backend.database.session import get_db
"""from backend.services.text_generator import generate_text
"""
from backend.services.gemini_text_generator import generate_text

from backend.api.dependecies.auth import get_current_user
from backend.database.models.user import User

router = APIRouter(
    prefix="/generate",
    tags=["Generate"]
)

@router.post("/text", response_model=GenerateResponse)
def generate(
    request: GenerateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = generate_text(
        db=db,
        user_id=current_user.id,
        prompt=request.prompt
    )

    return GenerateResponse(
        success=True,
        message="Text generated successfully.",
        generated_text=result["generated_text"],
        generated_text_id=result["generated_text_id"]
)