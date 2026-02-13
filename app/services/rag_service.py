from app.services.retrieval_service import retrieve_relevant_chunks
from app.services.prompt_service import build_prompt
from app.services.llm_service import generate_answer


def rag_answer(question: str, top_k: int = 4):
    chunks = retrieve_relevant_chunks(question, top_k)

    context = "\n\n".join(chunk.content for chunk in chunks)

    prompt = build_prompt(context, question)

    answer = generate_answer(prompt)

    return {
        "answer": answer,
        "sources": [{"chunk_id": c.id} for c in chunks]
    }