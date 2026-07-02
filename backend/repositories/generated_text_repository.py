from sqlalchemy.orm import Session
from sqlalchemy import text as sql_text

from backend.database.models import GeneratedText


class GeneratedTextRepository:

    @staticmethod
    def create(
        db: Session,
        user_id: int,
        prompt: str,
        generated_text: str
    ):

        # Debug
        print("Database:", db.execute(sql_text("SELECT current_database()")).scalar())
        print("Schema:", db.execute(sql_text("SELECT current_schema()")).scalar())

        generated_text_obj = GeneratedText(
            user_id=user_id,
            prompt=prompt,
            generated_text=generated_text
        )

        db.add(generated_text_obj)
        db.commit()
        db.refresh(generated_text_obj)

        return generated_text_obj

    @staticmethod
    def get_latest(
        db: Session,
        user_id: int
    ):

        return (
            db.query(GeneratedText)
            .filter(
                GeneratedText.user_id == user_id
            )
            .order_by(
                GeneratedText.created_at.desc()
            )
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
        user_id: int
    ):

        return (
            db.query(GeneratedText)
            .filter(
                GeneratedText.user_id == user_id
            )
            .order_by(
                GeneratedText.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        text_id: int
    ):

        text = (
            db.query(GeneratedText)
            .filter(
                GeneratedText.id == text_id
            )
            .first()
        )

        if text:
            db.delete(text)
            db.commit()

        return text