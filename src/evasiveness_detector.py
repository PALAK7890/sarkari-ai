from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from src.config import (
    SIMILARITY_MODEL,
    DIRECT_THRESHOLD,
    PARTIAL_THRESHOLD
)

print("Loading similarity model...")

model = SentenceTransformer(
    SIMILARITY_MODEL
)


def detect_evasiveness(question: str, reply: str):

    q_embedding = model.encode([question])

    r_embedding = model.encode([reply])

    similarity = cosine_similarity(
        q_embedding,
        r_embedding
    )[0][0]

    similarity = float(round(similarity, 3))

    if similarity >= DIRECT_THRESHOLD:

        verdict = "Direct Answer"

    elif similarity >= PARTIAL_THRESHOLD:

        verdict = "Partially Answered"

    else:

        verdict = "Highly Evasive"

    return {
        "score": similarity,
        "verdict": verdict
    }