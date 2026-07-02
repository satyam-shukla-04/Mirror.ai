from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from backend.database.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    last_login = Column(DateTime, nullable=True)

    documents = relationship(
    "Document",
    back_populates="user",
    cascade="all, delete-orphan"
)
    writing_profiles = relationship(
    "WritingProfile",
    cascade="all, delete-orphan"
)