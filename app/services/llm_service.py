from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="mistral",
    temperature=0,
    base_url="http://localhost:11434"
)


def generate_answer(prompt: str) -> str:
    return llm.invoke(prompt)
