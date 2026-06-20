from src.pipeline import analyze_document


question = """
How many vacancies were filled in 2024?
"""

reply = """
The information regarding recruitment and appointments
is available on the department website.
Relevant records may be accessed through the official portal.
"""


result = analyze_document(
    question,
    reply
)

print()

print("SUMMARY")
print(result["summary"])

print()

print("EVASIVENESS")
print(result["evasiveness"])

print()

print("ENTITIES")
print(result["entities"])