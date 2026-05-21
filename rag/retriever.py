import numpy as np
from sentence_transformers import SentenceTransformer

# Same embedding model for query
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query, index, chunks, k=3):
    """
    Retrieve top-k relevant chunks for a query.
    """
    if not query:
        return ""

    query_embedding = embedding_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, k)

    retrieved_chunks = [chunks[i] for i in indices[0] if i < len(chunks)]
    return "\n".join(retrieved_chunks)