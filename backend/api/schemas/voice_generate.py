from typing import Optional
from pydantic import BaseModel
from backend.api.schemas.common import APIResponse


class VoiceGenerateRequest(BaseModel):
    generated_text_id: Optional[int] = None
    custom_text: Optional[str] = None


class VoiceGenerateResponse(APIResponse):
    audio_path: str