from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    DateTime
)
from sqlalchemy.sql import func

from backend.database.base import Base


class GeneratedVoice(Base):

    __tablename__ = "generated_voices"

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

    generated_text_id = Column(
        Integer,
        ForeignKey("generated_texts.id"),
        nullable=False
    )

    audio_path = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )