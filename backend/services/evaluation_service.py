import json
import os

from dotenv import load_dotenv
from google import genai

from backend.repositories.profile_repositories import ProfileRepository
from backend.repositories.generated_text_repository import (
    GeneratedTextRepository
)
from backend.repositories.evaluation_repository import (
    EvaluationRepository
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def evaluate_text(
    db,
    user_id: int,
    generated_text_id: int
):
    """
    Evaluate how closely the generated text matches
    the user's writing style.
    """

    # Load writing profile
    profile = ProfileRepository.get_style_profile(
        db=db,
        user_id=user_id
    )

    # Load reference document
    reference = ProfileRepository.get_reference_text(
        db=db,
        user_id=user_id
    )

    # Load generated text
    generated = GeneratedTextRepository.get_by_id(
        db=db,
        text_id=generated_text_id
    )

    if generated is None:
        raise Exception("No generated text found.")

    prompt = f"""
You are an expert forensic linguist.

Compare the ORIGINAL WRITING and GENERATED WRITING.

Also consider the WRITING PROFILE.

STYLE PROFILE

{json.dumps(profile, indent=2)}

=====================================

ORIGINAL WRITING

{reference[:3000]}

=====================================

GENERATED WRITING

{generated.generated_text}

=====================================

Evaluate:

1. Overall Similarity (0-100)

2. Tone Match (0-100)

3. Vocabulary Match (0-100)

4. Sentence Structure (0-100)

5. Paragraph Flow (0-100)

6. Writing Habits (0-100)

7. Human Likeness (0-100)

Return ONLY valid JSON.

{{
    "overall_score": 0,
    "tone": 0,
    "vocabulary": 0,
    "sentence_structure": 0,
    "paragraph_flow": 0,
    "writing_habits": 0,
    "human_likeness": 0,
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}
"""

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
    print("\n========== GEMINI RESPONSE ==========")
    print(response.text)
    print("=====================================\n")

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")

    if text.startswith("```"):
        text = text.replace("```", "")

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    evaluation = json.loads(text)

    EvaluationRepository.create(
        db=db,
        user_id=user_id,
        generated_text_id=generated.id,
        overall_score=evaluation["overall_score"],
        evaluation=evaluation
    )

    return evaluation
