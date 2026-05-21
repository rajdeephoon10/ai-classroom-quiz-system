import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_store(chunks):
    """
    Create a FAISS vector store from text chunks.
    """
    if not chunks:
        raise ValueError("No text chunks provided for embedding.")

    embeddings = embedding_model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, chunks