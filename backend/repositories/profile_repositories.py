import json

from backend.repositories.document_repository import DocumentRepository
from backend.repositories.writing_profile_repository import (
    WritingProfileRepository
)

from backend.repositories.voice_profile_repository import VoiceProfileRepository
class ProfileRepository:

    @staticmethod
    def get_style_profile(
        db,
        user_id: int
    ):

        profile = WritingProfileRepository.get_latest(
            db=db,
            user_id=user_id
        )

        if profile is None:
            raise Exception(
                "No writing profile found."
            )

        return json.loads(
            profile.profile_json
        )

    @staticmethod
    def get_reference_text(
        db,
        user_id: int
    ):

        document = DocumentRepository.get_latest(
            db=db,
            user_id=user_id
        )

        if document is None:
            raise Exception(
                "No uploaded document found."
            )

        return document.extracted_text
    @staticmethod
    def get_voice_profile(
    db,
    user_id: int
):

     profile = VoiceProfileRepository.get_latest(
        db=db,
        user_id=user_id
    )

     if profile is None:
        raise Exception("No voice profile found.")

     return profile