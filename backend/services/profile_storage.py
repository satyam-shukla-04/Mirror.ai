import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PROFILE_DIR = BASE_DIR / "data" / "profiles"

PROFILE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def save_profile(profile):

    file_path = PROFILE_DIR / "style_profile.json"

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        #profile = json.loads(profile)

        json.dump(profile, f, indent=4)

    print("Profile Saved:", file_path)

    return file_path