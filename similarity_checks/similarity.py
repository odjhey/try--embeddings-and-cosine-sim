from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .db import fetch_embedding


# Calculate cosine similarity
def calculate_similarity(embedding1, embedding2):
    # Ensure embeddings are in the correct shape
    embedding1 = np.array(embedding1).reshape(1, -1)
    embedding2 = np.array(embedding2).reshape(1, -1)
    return cosine_similarity(embedding1, embedding2)[0][0]


