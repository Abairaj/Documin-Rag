from sentence_transformers import SentenceTransformer
from typing import List

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(text_chunks:List[str]):
    return model.encode(text_chunks).tolist()