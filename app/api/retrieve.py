from fastapi import APIRouter
from app.services.retrieval_service import retrieve_relevant_chunks

router = APIRouter(
    prefix='/retrieve',
    tags = ['Retrieval']
)

@router.post('/')
def retrieve(query:str):
    chunks = retrieve_relevant_chunks(query)

    return {
        "query": query,
        "results": [
            {
                "chunk_id": c.id,
                "content": c.content
            }
            for c in chunks
        ]
    }