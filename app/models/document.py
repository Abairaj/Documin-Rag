from app.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum as SqlEnum
from datetime import datetime
from enum import Enum


class DocumentStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    completed = "completed"
    failed = "failed"


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    s3_key = Column(String)
    status = Column(
        SqlEnum(DocumentStatus, name="document_status"),
        default=DocumentStatus.pending,
        nullable=False,
    )
    time_created = Column(DateTime, default=datetime.now)
