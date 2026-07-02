from sqlalchemy.orm import Session

from backend.database.models import Document


class DocumentRepository:

    @staticmethod
    def create(
        db: Session,
        document: Document
    ):

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def get_latest(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Document)
            .filter(Document.user_id == user_id)
            .order_by(Document.uploaded_at.desc())
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Document)
            .filter(Document.user_id == user_id)
            .all()
        )