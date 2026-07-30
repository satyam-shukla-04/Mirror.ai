import os
from pathlib import Path
from datetime import datetime
from typing import Optional

from backend.services.omnivoice_service import OmniVoiceService

from backend.repositories.profile_repositories import ProfileRepository
from backend.repositories.generated_text_repository import GeneratedTextRepository
from backend.repositories.generated_voice_repository import GeneratedVoiceRepository


UPLOAD_DIR = Path("uploads/generated_voice")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def generate_voice(
    db,
    user_id: int,
    generated_text_id: Optional[int] = None,
    custom_text: Optional[str] = None,
):
    """
    Generate cloned speech using either:
    1. Existing generated text
    2. Custom text entered by the user
    """

    # ---------------------------------
    # Load latest voice profile
    # ---------------------------------

    voice_profile = ProfileRepository.get_voice_profile(
        db=db,
        user_id=user_id,
    )

    if voice_profile is None:
        raise Exception("No voice profile found.")

    reference_audio = voice_profile.audio_path

    if not os.path.exists(reference_audio):
        raise Exception("Reference audio not found.")

    # ---------------------------------
    # Decide which text to use
    # ---------------------------------

    if generated_text_id is not None:

        generated = GeneratedTextRepository.get_by_id(
            db=db,
            text_id=generated_text_id,
        )

        if generated is None:
            raise Exception("Generated text not found.")

    elif custom_text:

        generated = GeneratedTextRepository.create(
            db=db,
            user_id=user_id,
            prompt="Custom Voice Input",
            generated_text=custom_text,
        )

    else:

        raise Exception(
            "Please provide generated_text_id or custom_text."
        )

    # ---------------------------------
    # Output filename
    # ---------------------------------

    filename = (
        f"user_{user_id}_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    )

    output_path = UPLOAD_DIR / filename

    # ---------------------------------
    # Generate cloned voice
    # ---------------------------------

    OmniVoiceService.generate(
        text=generated.generated_text,
        reference_audio=str(reference_audio),
        output_path=str(output_path),
    )

    # ---------------------------------
    # Save generated voice
    # ---------------------------------

    voice = GeneratedVoiceRepository.create(
        db=db,
        user_id=user_id,
        generated_text_id=generated.id,
        audio_path=str(output_path),
    )

    return voice