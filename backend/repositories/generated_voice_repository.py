from sqlalchemy.orm import Session

from backend.database.models import GeneratedVoice


class GeneratedVoiceRepository:

    @staticmethod
    def create(
        db: Session,
        user_id: int,
        generated_text_id: int,
        audio_path: str,
    ):

        voice = GeneratedVoice(
            user_id=user_id,
            generated_text_id=generated_text_id,
            audio_path=audio_path,
        )

        db.add(voice)
        db.commit()
        db.refresh(voice)

        return voice

    @staticmethod
    def get_latest(
        db: Session,
        user_id: int,
    ):

        return (
            db.query(GeneratedVoice)
            .filter(
                GeneratedVoice.user_id == user_id
            )
            .order_by(
                GeneratedVoice.created_at.desc()
            )
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
        user_id: int,
    ):

        return (
            db.query(GeneratedVoice)
            .filter(
                GeneratedVoice.user_id == user_id
            )
            .order_by(
                GeneratedVoice.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        voice_id: int,
    ):

        return (
            db.query(GeneratedVoice)
            .filter(
                GeneratedVoice.id == voice_id
            )
            .first()
        )