import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.database.models.user import User
from backend.api.dependecies.auth import get_current_user

from backend.services.evaluation_service import evaluate_text
from backend.repositories.evaluation_repository import EvaluationRepository

from backend.api.schemas.evaluation import (
    EvaluationRequest,
    EvaluationResponse
)

from backend.api.schemas.evaluation_history import (
    EvaluationHistoryResponse,
    EvaluationItem
)


router = APIRouter(
    prefix="/evaluate",
    tags=["Evaluation"]
)


@router.post(
    "/text",
    response_model=EvaluationResponse
)
def evaluate(
    request: EvaluationRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = evaluate_text(
        db=db,
        user_id=current_user.id,
        generated_text_id=request.generated_text_id
    )

    return EvaluationResponse(
        success=True,
        message="Evaluation completed successfully.",
        evaluation=result
    )


@router.get(
    "/history",
    response_model=EvaluationHistoryResponse
)
def history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    evaluations = EvaluationRepository.get_all(
        db=db,
        user_id=current_user.id
    )

    items = [
        EvaluationItem(
            id=evaluation.id,
            overall_score=evaluation.overall_score,
            created_at=str(evaluation.created_at)
        )
        for evaluation in evaluations
    ]

    return EvaluationHistoryResponse(
        success=True,
        message="Evaluation history retrieved.",
        evaluations=items
    )


@router.get("/{evaluation_id}")
def get_evaluation(
    evaluation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    evaluation = EvaluationRepository.get_by_id(
        db=db,
        evaluation_id=evaluation_id
    )

    if evaluation is None:
        raise HTTPException(
            status_code=404,
            detail="Evaluation not found."
        )

    if evaluation.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied."
        )

    return {
        "success": True,
        "message": "Evaluation retrieved successfully.",
        "evaluation": json.loads(
            evaluation.evaluation_json
        )
    }


@router.delete("/{evaluation_id}")
def delete_evaluation(
    evaluation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    evaluation = EvaluationRepository.get_by_id(
        db=db,
        evaluation_id=evaluation_id
    )

    if evaluation is None:
        raise HTTPException(
            status_code=404,
            detail="Evaluation not found."
        )

    if evaluation.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied."
        )

    EvaluationRepository.delete(
        db=db,
        evaluation_id=evaluation_id
    )

    return {
        "success": True,
        "message": "Evaluation deleted successfully."
    }