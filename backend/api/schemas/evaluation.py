from pydantic import BaseModel
from backend.api.schemas.common import APIResponse


class EvaluationRequest(BaseModel):
    generated_text_id: int


class EvaluationResponse(APIResponse):
    evaluation: dict