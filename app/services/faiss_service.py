import faiss
import os
import numpy as np

INDEX_PATH = "faiss_index/index.faiss"

dimension = 384

if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
else:
    index = faiss.IndexFlatL2(dimension)


def save_vectors(vectors):
    global index

    vectors = np.array(vectors).astype("float32")
    index.add(vectors)

    os.makedirs("faiss_index", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)


def search_vectors(query_vector,top_k=5):
    query_vector = np.array([query_vector]).astype('float32')
    _,indices = index.search(query_vector,top_k)
    return indices[0]
