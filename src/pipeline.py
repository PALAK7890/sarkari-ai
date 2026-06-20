from src.summarizer import generate_summary
from src.evasiveness_detector import detect_evasiveness
from src.entity_extractor import extract_entities
from src.followup_generator import generate_followup


def analyze_document(question, reply):

    summary = generate_summary(reply)

    evasiveness = detect_evasiveness(
        question,
        reply
    )

    entities = extract_entities(
        reply
    )

    followup = generate_followup(
        question
    )

    return {

        "summary": summary,

        "evasiveness": evasiveness,

        "entities": entities,

        "followup": followup

    }