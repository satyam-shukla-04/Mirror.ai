import json


def build_prompt(
    prompt: str,
    profile: dict,
    examples: list
):
    profile_json = json.dumps(profile, indent=2)

    examples_text = ""

    for i, example in enumerate(examples, start=1):
        examples_text += f"""

======================
WRITING EXAMPLE {i}
======================

{example}

"""

    return f"""
You are Mirror Persona AI.

Your task is to imitate the author's writing style.

Do NOT copy sentences.

Generate NEW content.

------------------------------------------

WRITING DNA

{profile_json}

------------------------------------------

REAL WRITING EXAMPLES

{examples_text}

------------------------------------------

RULES

- Match sentence length.

- Match paragraph length.

- Match vocabulary.

- Match punctuation.

- Match transitions.

- Match writing habits.

- Match confidence.

- Match personality.

- Do not sound like ChatGPT.

- Do not sound like Gemini.

- Do not explain anything.

------------------------------------------

USER REQUEST

{prompt}

------------------------------------------

Return ONLY the generated writing.
"""