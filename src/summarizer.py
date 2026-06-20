from transformers import pipeline
from src.config import (
    SUMMARIZATION_MODEL,
    MAX_SUMMARY_LENGTH,
    MIN_SUMMARY_LENGTH
)

print("Loading summarization model...")

summarizer = pipeline(
    "summarization",
    model=SUMMARIZATION_MODEL
)


def generate_summary(text: str) -> str:
    """
    Generate a plain-English summary.
    """

    result = summarizer(
        text,
        max_length=MAX_SUMMARY_LENGTH,
        min_length=MIN_SUMMARY_LENGTH,
        do_sample=False
    )

    return result[0]["summary_text"]