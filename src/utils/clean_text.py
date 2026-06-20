import re


def clean_text(text: str) -> str:
    """
    Clean unwanted spaces and symbols.
    """

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text