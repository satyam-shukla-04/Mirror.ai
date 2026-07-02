import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_style_with_groq(text: str):
    """
    Analyze the author's writing and generate a comprehensive
    Writing DNA profile for Mirror Persona AI.

    Returns ONLY valid JSON.
    """

    prompt = f"""
You are an expert forensic linguist, computational stylist,
writing coach, and AI persona cloning specialist.

Your job is NOT to summarize the content.

Your job is to understand HOW the author writes.

Analyze every characteristic that makes this person's writing unique.

Study:

• Writing personality
• Thinking process
• Tone
• Formality
• Emotional expression
• Vocabulary
• Word choices
• Favorite words
• Common phrases
• Sentence length
• Sentence complexity
• Paragraph structure
• Logical flow
• Storytelling style
• Persuasion style
• Technical depth
• Humor
• Confidence
• Opening style
• Closing style
• Formatting habits
• Punctuation
• Capitalization
• Transition words
• Writing habits
• Grammar habits
• Repetition
• Signature patterns
• Human imperfections
• Typical mistakes
• Call-to-action style
• Question usage

Return ONLY VALID JSON.

Never explain.

Never use markdown.

If a field cannot be determined,
return "Unknown".

Return EXACTLY this schema:

{{
    "author_identity": {{
        "communication_role": "",
        "primary_goal": "",
        "target_audience": "",
        "expertise_level": "",
        "communication_purpose": ""
    }},

    "style_summary":"",

    "tone":"",

    "writing_personality":"",

    "formality":"",

    "confidence_level":"",

    "emotion_level":"",

    "humor_level":"",

    "persuasiveness":"",

    "technical_level":"",

    "thinking_style": {{
        "logical":"",
        "analytical":"",
        "story_driven":"",
        "reflective":"",
        "opinion_based":"",
        "fact_based":"",
        "step_by_step":""
    }},

    "writing_statistics": {{
        "average_sentence_length":"",
        "average_paragraph_length":"",
        "sentence_complexity":"",
        "active_vs_passive_voice":"",
        "question_frequency":"",
        "list_usage":"",
        "heading_usage":""
    }},

    "vocabulary_profile": {{
        "common_words":[],
        "technical_terms":[],
        "transition_words":[],
        "power_words":[],
        "filler_words":[],
        "words_to_avoid":[]
    }},

    "favorite_words":[],

    "frequently_used_phrases":[],

    "sentence_style":"",

    "paragraph_style":"",

    "storytelling_style":"",

    "argument_style":"",

    "question_usage":"",

    "call_to_action_style":"",

    "opening_style":"",

    "closing_style":"",

    "punctuation_style":"",

    "capitalization_style":"",

    "emoji_usage":"",

    "formatting_style":"",

    "grammar_style":"",

    "signature_patterns":[],

    "writing_habits":[],

    "common_mistakes":[],

    "style_constraints": {{
        "always_do":[],
        "never_do":[],
        "maintain":[]
    }},

    "analysis_confidence": {{
        "tone":"",
        "vocabulary":"",
        "storytelling":"",
        "overall":""
    }},

    "few_shot_examples":[
        {{
            "purpose":"Opening",
            "text":""
        }},
        {{
            "purpose":"Explanation",
            "text":""
        }},
        {{
            "purpose":"Opinion",
            "text":""
        }},
        {{
            "purpose":"Closing",
            "text":""
        }}
    ]
}}

Analyze ONLY the writing style.

Do NOT summarize the topic.

Here is the writing sample:

{text[:12000]}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a forensic linguistics expert. "
                    "Return ONLY valid JSON."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.choices[0].message.content