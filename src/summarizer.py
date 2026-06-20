from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from src.config import *

tokenizer = None
model = None


def load_model():
    global tokenizer, model

    if tokenizer is None:

        print("Loading FLAN-T5...")

        tokenizer = AutoTokenizer.from_pretrained(
            SUMMARIZATION_MODEL
        )

        model = AutoModelForSeq2SeqLM.from_pretrained(
            SUMMARIZATION_MODEL
        )


def generate_summary(text):

    load_model()

    prompt = f"""
    Summarize the following text.
    Use only information present in the text.
    Do not add facts.

    Text:
    {text}
    """

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return summary