import json

from sqlalchemy.orm import Session

from backend.database.models import Evaluation


class EvaluationRepository:

    @staticmethod
    def create(
        db: Session,
        user_id: int,
        generated_text_id: int,
        overall_score: int,
        evaluation: dict
    ):

        evaluation_obj = Evaluation(
            user_id=user_id,
            generated_text_id=generated_text_id,
            overall_score=overall_score,
            evaluation_json=json.dumps(evaluation)
        )

        db.add(evaluation_obj)
        db.commit()
        db.refresh(evaluation_obj)

        return evaluation_obj

    @staticmethod
    def get_latest(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Evaluation)
            .filter(
                Evaluation.user_id == user_id
            )
            .order_by(
                Evaluation.created_at.desc()
            )
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Evaluation)
            .filter(
                Evaluation.user_id == user_id
            )
            .order_by(
                Evaluation.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_by_generated_text(
        db: Session,
        generated_text_id: int
    ):

        return (
            db.query(Evaluation)
            .filter(
                Evaluation.generated_text_id == generated_text_id
            )
            .first()
        )

    @staticmethod
    def get_by_id(
    db: Session,
    evaluation_id: int
):

        return (
        db.query(Evaluation)
        .filter(
            Evaluation.id == evaluation_id
        )
        .first()
    )


    @staticmethod
    def delete(
        db: Session,
        evaluation_id: int
    ):

        evaluation = (
            db.query(Evaluation)
            .filter(
                Evaluation.id == evaluation_id
            )
            .first()
        )

        if evaluation:
            db.delete(evaluation)
            db.commit()

        return evaluation