import streamlit as st

from src.pipeline import analyze_document

st.set_page_config(
    page_title="Sarkari Speak",
    page_icon="🇮🇳"
)

st.title("🇮🇳 Sarkari Speak")

question = st.text_area(
    "RTI Question"
)

reply = st.text_area(
    "RTI Reply"
)

if st.button("Analyze"):

    result = analyze_document(
        question,
        reply
    )

    st.subheader("Plain English Summary")

    st.write(
        result["summary"]
    )

    st.subheader("Evasiveness")

    st.json(
        result["evasiveness"]
    )

    st.subheader("Entities")

    st.json(
        result["entities"]
    )

    st.subheader("Suggested Follow-up RTI")

    st.write(
        result["followup"]
    )