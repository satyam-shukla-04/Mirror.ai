from pydantic import BaseModel
from backend.api.schemas.common import APIResponse


class EvaluationItem(BaseModel):

    id: int
    overall_score: int
    created_at: str

    class Config:
        from_attributes = True


class EvaluationHistoryResponse(APIResponse):

    evaluations: list[EvaluationItem]