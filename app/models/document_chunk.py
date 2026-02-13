from sqlalchemy import Column,Integer,ForeignKey,Text
from app.db.base import Base

class DocumentChunk(Base):
    __tablename__ = 'document_chunks'

    id = Column(Integer,primary_key=True,db_index=True)
    document_id = Column(Integer,ForeignKey('documents.id'))
    chunk_index = Column(Integer)
    content = Column(Text)