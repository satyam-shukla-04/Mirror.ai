from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.repositories.user_repository import UserRepository
from backend.utils.jwt_handler import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    user = db.get(
        UserRepository.model,
        int(user_id)
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user