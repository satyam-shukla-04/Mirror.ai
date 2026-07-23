from pydantic import BaseModel
from backend.api.schemas.common import APIResponse


class VoiceGenerateRequest(BaseModel):
    generated_text_id: int


class VoiceGenerateResponse(APIResponse):
    audio_path: str