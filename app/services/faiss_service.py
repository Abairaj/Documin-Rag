import faiss
import os
import numpy as np

INDEX_PATH = "faiss_index/index.faiss"

dimension = 384
index = faiss.IndexFlatL2(dimension)


def save_vectors(vectors):
    global index

    vectors = np.array(vectors).astype("float32")
    index.add(vectors)

    os.makedirs("faiss_index", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
