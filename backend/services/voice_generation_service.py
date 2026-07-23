import os
from pathlib import Path
from datetime import datetime

from backend.services.omnivoice_service import OmniVoiceService

from backend.repositories.profile_repositories import ProfileRepository
from backend.repositories.generated_text_repository import GeneratedTextRepository
from backend.repositories.generated_voice_repository import GeneratedVoiceRepository


UPLOAD_DIR = Path("uploads/generated_voice")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def generate_voice(
    db,
    user_id: int,
    generated_text_id: int,
):
    """
    Generate cloned speech from a previously generated text.
    """

    # -------------------------------
    # Load latest voice reference
    # -------------------------------

    voice_profile = ProfileRepository.get_voice_profile(
        db=db,
        user_id=user_id
    )

    if voice_profile is None:
        raise Exception("No voice profile found.")

    reference_audio = voice_profile.audio_path

    if not os.path.exists(reference_audio):
        raise Exception("Reference audio not found.")

    # -------------------------------
    # Load generated text
    # -------------------------------

    generated = GeneratedTextRepository.get_by_id(
        db=db,
        text_id=generated_text_id
    )

    if generated is None:
        raise Exception("Generated text not found.")

    # -------------------------------
    # Output filename
    # -------------------------------

    filename = (
        f"user_{user_id}_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    )

    output_path = UPLOAD_DIR / filename

    # -------------------------------
    # Generate voice
    # -------------------------------

    OmniVoiceService.generate(
        text=generated.generated_text,
        reference_audio=str(reference_audio),
        output_path=str(output_path),
    )

    # -------------------------------
    # Save to database
    # -------------------------------

    voice = GeneratedVoiceRepository.create(
        db=db,
        user_id=user_id,
        generated_text_id=generated.id,
        audio_path=str(output_path),
    )

    return voice