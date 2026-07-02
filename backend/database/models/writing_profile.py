from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
    DateTime
)

from backend.database.base import Base


class WritingProfile(Base):

    __tablename__ = "writing_profiles"

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

    profile_json = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )