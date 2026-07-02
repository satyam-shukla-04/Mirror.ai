from pydantic import BaseModel, EmailStr
from backend.api.schemas.common import APIResponse


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(APIResponse):
    user_id: int
    username: str
    email: EmailStr


class LoginResponse(APIResponse):
    access_token: str
    token_type: str