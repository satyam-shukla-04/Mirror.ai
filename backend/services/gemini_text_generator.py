import os

from dotenv import load_dotenv
from google import genai

from backend.services.profile_loader import load_profile
from backend.services.prompt_builder import build_prompt
from backend.repositories.generated_text_repository import (
    GeneratedTextRepository
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_text(
    db,
    user_id: int,
    prompt: str
):

    profile, examples = load_profile(
        db=db,
        user_id=user_id
    )

    full_prompt = build_prompt(
        prompt=prompt,
        profile=profile,
        examples=examples
    )

    print("\n========== GEMINI ==========")
    print(full_prompt[:1000])
    print("============================\n")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    generated_text = response.text.strip()

    GeneratedTextRepository.create(
        db=db,
        user_id=user_id,
        prompt=prompt,
        generated_text=generated_text
    )

    return generated_text