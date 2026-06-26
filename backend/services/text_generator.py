import json
import os
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_text(prompt):
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    REFERENCE_FILE = (
    BASE_DIR
    / "data"
    / "extracted_text"
    / "writing_reference.txt"
)

    with open(
    REFERENCE_FILE,
    "r",
    encoding="utf-8"
) as f:

        reference_text = f.read()

    with open(
        "../data/profiles/style_profile.json",
        "r",
        encoding="utf-8"
    ) as f:

        profile = json.load(f)
    

    full_prompt = f"""
You are Mirror AI.

Your task is to imitate the user's writing style while producing the correct document format.

STYLE PROFILE:
{json.dumps(profile, indent=2)}


User Request:
{prompt}
RULES:

1. Follow the requested content type exactly.
2. If the user asks for an EMAIL:
   - Start with Subject:
   - Then greeting (e.g., Dear Sir/Madam,)
   - Then the email body
   - Then closing (Regards, Thanks, etc.)
3. If the user asks for a LinkedIn post, output only a LinkedIn post.
4. If the user asks for a blog, output only a blog.
5. Never explain the style.
6. Never output JSON.
7. Return only the requested content.
"""

    print("PROFILE:")
    print(profile)

    print("\nFULL PROMPT LENGTH:")
    print(len(full_prompt))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content