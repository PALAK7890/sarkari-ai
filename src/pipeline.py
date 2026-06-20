from src.summarizer import generate_summary

from src.evasiveness_detector import detect_evasiveness

from src.entity_extractor import extract_entities


def analyze_document(
        question: str,
        reply: str
):

    summary = generate_summary(reply)

    evasiveness = detect_evasiveness(
        question,
        reply
    )

    entities = extract_entities(
        reply
    )

    return {

        "summary": summary,

        "evasiveness": evasiveness,

        "entities": entities
    }