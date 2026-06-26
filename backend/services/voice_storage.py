import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PROFILE_DIR = BASE_DIR / "data" / "profiles"
PROFILE_DIR.mkdir(parents=True, exist_ok=True)


def save_voice_profile(profile):

    file_path = PROFILE_DIR / "voice_profile.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4)

    return file_path