def generate_followup(question):

    followup = f"""
Please provide a specific response to the following RTI query:

{question}

Kindly furnish the information in tabular format under Section 2(f) of the RTI Act, 2005.
"""

    return followup.strip()