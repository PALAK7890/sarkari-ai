import spacy
from src.config import *

nlp = None


def load_model():

    global nlp

    if nlp is None:

        print("Loading spaCy model...")

        nlp = spacy.load(
            SPACY_MODEL
        )


def extract_entities(text):

    load_model()

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