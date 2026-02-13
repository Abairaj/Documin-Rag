from fastapi import APIRouter
from app.services.rag_service import rag_answer

router = APIRouter()

@router.post("/")
def chat(question: str):
    model_output =  rag_answer(question)

    answer = model_output.get('answer',{})
    answer_content = getattr(answer,'content',"")

    return {"answer":answer_content}