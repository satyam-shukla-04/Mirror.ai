from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
    DateTime
)

from backend.database.base import Base


class GeneratedText(Base):

    __tablename__ = "generated_texts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    prompt = Column(
        Text,
        nullable=False
    )

    generated_text = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )