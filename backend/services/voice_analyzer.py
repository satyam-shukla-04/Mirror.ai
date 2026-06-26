from backend.services.audio_features import (
    load_audio,
    get_duration,
    get_sample_rate,
    get_channels,
    get_format,
    get_average_pitch,
    get_average_volume,
    get_silence_ratio
)


def analyze_voice(file_path):

    y, sr = load_audio(file_path)

    profile = {

        "duration": get_duration(y, sr),

        "sample_rate": get_sample_rate(sr),

        "channels": get_channels(file_path),

        "format": get_format(file_path),

        "average_pitch_hz": get_average_pitch(y, sr),

        "average_volume": get_average_volume(y),

        "silence_ratio": get_silence_ratio(y)

    }

    return profile