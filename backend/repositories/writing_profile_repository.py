import json

from sqlalchemy.orm import Session

from backend.database.models import WritingProfile


class WritingProfileRepository:

    @staticmethod
    def create(
        db: Session,
        user_id: int,
        profile: dict
    ):

        writing_profile = WritingProfile(
            user_id=user_id,
            profile_json=json.dumps(profile)
        )

        db.add(writing_profile)
        db.commit()
        db.refresh(writing_profile)

        return writing_profile

    @staticmethod
    def get_latest(
        db: Session,
        user_id: int
    ):

        return (
            db.query(WritingProfile)
            .filter(WritingProfile.user_id == user_id)
            .order_by(WritingProfile.created_at.desc())
            .first()
        )