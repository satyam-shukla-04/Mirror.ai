from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.schemas.auth import (
    RegisterRequest,
    AuthResponse,
    LoginRequest,
    LoginResponse
)
from backend.services.auth_service import login_user
from backend.database.session import get_db
from backend.services.auth_service import register_user
from backend.api.dependecies.auth import get_current_user
from backend.database.models.user import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }

@router.post(
    "/register",
    response_model=AuthResponse
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    try:

        user = register_user(
            db=db,
            username=request.username,
            email=request.email,
            password=request.password
        )

        return AuthResponse(
            success=True,
            message="User registered successfully.",
            user_id=user.id,
            username=user.username,
            email=user.email
        )

    except ValueError as e:
        print("REGISTER ERROR:", e)

        raise HTTPException(
            status_code=400,
             detail=str(e)
    )

@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    try:

        token = login_user(
            db=db,
            email=request.email,
            password=request.password
        )

        return LoginResponse(
            success=True,
            message="Login successful.",
            access_token=token,
            token_type="Bearer"
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
    
@router.post("/token")
def token_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:

        token = login_user(
            db=db,
            email=form_data.username,   # Email goes here
            password=form_data.password
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )