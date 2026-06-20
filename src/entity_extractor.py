import spacy

from src.config import SPACY_MODEL

nlp = spacy.load(
    SPACY_MODEL
)


def extract_entities(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        entities.append(
            {
                "entity": ent.text,
                "label": ent.label_
            }
        )

    return entities