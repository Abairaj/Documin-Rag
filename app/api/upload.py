from fastapi import APIRouter,UploadFile
from app.services.s3_service import upload_file
from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.faiss_service import save_vectors
from app.db.session import SessionLocal
from app.models.document import Document
import pdfplumber
import uuid

router = APIRouter()

@router.post("/documents/upload")
async def upload_document(file:UploadFile):
    db = SessionLocal()

    key = f"docs/{uuid.uuid4()}_{file.filename}"
    upload_file(file.file,key)    
    doc = Document(filename=file.filename,s3_key=key)
    db.add(doc)
    db.commit()
    db.refresh(doc)

    text = ""

    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()
    

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    save_vectors(embeddings)

    doc.status = "completed"
    db.commit()

    return {"message":"Document indexed successfully", "chunks":len(chunks)}