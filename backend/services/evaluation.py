import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

STYLE_PROFILE = BASE_DIR / "data" / "profiles" / "style_profile.json"
VOICE_PROFILE = BASE_DIR / "data" / "profiles" / "voice_profile.json"

WRITING_REF = BASE_DIR / "data" / "extracted_text" / "writing_reference.txt"
VOICE_REF = BASE_DIR / "uploads" / "audio" / "voice_reference.wav"


def load_json(path):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def evaluate_persona():

    style = load_json(STYLE_PROFILE)
    voice = load_json(VOICE_PROFILE)

    report = {

        "writing_reference": WRITING_REF.exists(),

        "voice_reference": VOICE_REF.exists(),

        "style_profile": style is not None,

        "voice_profile": voice is not None,

        "persona_ready": (
            WRITING_REF.exists()
            and VOICE_REF.exists()
            and style is not None
            and voice is not None
        ),

        "style": style,

        "voice": voice

    }
    print(type(style))
    print(style)

    print(type(voice))
    print(voice)
    return report