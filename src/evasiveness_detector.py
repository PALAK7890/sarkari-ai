from sentence_transformers import CrossEncoder
from scipy.special import expit

from src.config import *

cross_encoder = None


def load_model():
    global cross_encoder

    if cross_encoder is None:
        print("Loading CrossEncoder...")
        cross_encoder = CrossEncoder(CROSS_ENCODER_MODEL)


def detect_evasiveness(question, reply):

    load_model()

    logit = cross_encoder.predict(
        [(question, reply)]
    )[0]

    score = float(expit(logit))

    if score >= DIRECT_THRESHOLD:
        verdict = "Direct Answer"

    elif score >= PARTIAL_THRESHOLD:
        verdict = "Partially Answered"

    else:
        verdict = "Highly Evasive"

    return {
        "score": round(score, 3),
        "verdict": verdict
    }