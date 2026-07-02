from backend.api.schemas.common import APIResponse


class UploadResponse(APIResponse):
    file_path: str | None = None
    profile_created: bool = False


class VoiceUploadResponse(APIResponse):
    file_path: str | None = None
    voice_profile_created: bool = False