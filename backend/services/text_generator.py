import os
from dotenv import load_dotenv
from groq import Groq

from backend.services.profile_loader import load_profile
from backend.services.prompt_builder import build_prompt
from backend.repositories.generated_text_repository import (
    GeneratedTextRepository)
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_text(
    db,
    user_id: int,
    prompt: str
):
    """
    Generate text in the user's writing style.
    """

    # Load user's learned style
    profile, examples = load_profile(
        db=db,
        user_id=user_id
    )

    full_prompt = build_prompt(
        prompt=prompt,
        profile=profile,
        examples=examples
    )

    print("\n========== PROFILE ==========")
    print(profile)

    print("\n========== EXAMPLES ==========")

    for i, example in enumerate(examples):
        print(f"\nExample {i+1}\n")
        print(example[:300])

    print("==============================")
    # Generate response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ],
        temperature=0.7,
        max_tokens=500
    )

    generated_text = response.choices[0].message.content.strip()

    


    GeneratedTextRepository.create(
    db=db,
    user_id=user_id,
    prompt=prompt,
    generated_text=generated_text
)

    return generated_text
