from backend.database.models.voice_profile import VoiceProfile


class VoiceProfileRepository:

    @staticmethod
    def create(db, user_id: int, audio_path: str):

        voice = VoiceProfile(
            user_id=user_id,
            audio_path=audio_path
        )

        db.add(voice)
        db.commit()
        db.refresh(voice)

        return voice

    @staticmethod
    def get_latest(db, user_id: int):

        return (
            db.query(VoiceProfile)
            .filter(
                VoiceProfile.user_id == user_id
            )
            .order_by(
                VoiceProfile.created_at.desc()
            )
            .first()
        )