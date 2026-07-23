from pydantic import BaseModel
from backend.api.schemas.common import APIResponse


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(APIResponse):
    generated_text: str
    generated_text_id: int