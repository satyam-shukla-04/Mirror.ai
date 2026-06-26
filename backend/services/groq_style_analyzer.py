import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_style_with_groq(text):

    prompt = f"""
Analyze the writing style.

Return ONLY valid JSON.

{{
  "style_summary": "...",

  "tone": "...",

  "formality": "...",

  "sentence_structure": "...",

  "vocabulary": "...",

  "common_phrases": [...],

  "opening_style": "...",

  "closing_style": "...",

  "emoji_usage": "...",

  "punctuation_style": "...",

  "writing_habits": [...],

  "dos_and_donts": [...],

  "few_shot_examples": [
      "...",
      "...",
      "..."
  ]
}}

Writing Sample:

{text[:5000]}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content