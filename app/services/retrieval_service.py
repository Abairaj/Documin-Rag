from app.services.embedding_service import generate_embeddings
from app.services.faiss_service import search_vectors
from app.models.document_chunk import DocumentChunk
from app.db.session import SessionLocal


def retrieve_relevant_chunks(query:str,top_k:int=5):
    
    db = SessionLocal()

    query_embedding = generate_embeddings([query])[0]
    indices = search_vectors(query_embedding,top_k)

    list_indices = list(map(int, indices))

    chunks = db.query(DocumentChunk).filter(
        DocumentChunk.id.in_(list_indices)
    ).all()

    return chunks