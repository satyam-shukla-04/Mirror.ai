# backend/services/audio_features.py

import librosa
import numpy as np


def load_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    return y, sr


def get_duration(y, sr):
    return round(len(y) / sr, 2)


def get_sample_rate(sr):
    return sr


def get_channels(file_path):
    import soundfile as sf

    info = sf.info(file_path)
    return info.channels


def get_format(file_path):
    return file_path.split(".")[-1]


def get_average_pitch(y, sr):

    pitches, magnitudes = librosa.piptrack(
        y=y,
        sr=sr
    )

    pitch_values = pitches[pitches > 0]

    if len(pitch_values) == 0:
        return 0

    return round(float(np.mean(pitch_values)), 2)


def get_average_volume(y):

    rms = librosa.feature.rms(y=y)

    return round(float(np.mean(rms)), 4)


def get_silence_ratio(y):

    intervals = librosa.effects.split(y)

    speech_samples = sum(
        end - start
        for start, end in intervals
    )

    total_samples = len(y)

    silence_samples = total_samples - speech_samples

    return round(silence_samples / total_samples, 2)