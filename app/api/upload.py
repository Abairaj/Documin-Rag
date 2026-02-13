from fastapi import APIRouter,UploadFile
from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.faiss_service import save_vectors
from app.db.session import SessionLocal
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
import pdfplumber
import uuid
import io

router = APIRouter()

@router.post("/documents/upload")
async def upload_document(file:UploadFile):    
    file_name = file.filename
    file_content = await file.read()

    # duplicate stream writing is here have to find the standard way
    # upload_stream = io.BytesIO(file_content)
    process_stream = io.BytesIO(file_content)

    key = f"docs/{uuid.uuid4()}_{file_name}"
    # upload_file(upload_stream,key)

    db = SessionLocal()
    doc = Document(filename=file_name,s3_key=key)
    db.add(doc)
    db.commit()
    db.refresh(doc)

    text = ""

    with pdfplumber.open(process_stream) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()
    

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    for idx,chunk in enumerate(chunks):
        db_chunk = DocumentChunk(
            document_id=doc.id,
            chunk_index = idx,
            content=chunk
        )
        db.add(db_chunk)

    save_vectors(embeddings)

    doc.status = "completed"
    db.commit()
    return {"message":"Document indexed successfully", "chunks":len(chunks)}