import os
from pathlib import Path

import soundfile as sf
import torch
from omnivoice import OmniVoice


class OmniVoiceService:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            print("\nLoading OmniVoice model...\n")

            cls._model = OmniVoice.from_pretrained(
                "k2-fsa/OmniVoice",
                device_map="cpu",
                dtype=torch.float32
            )

            print("\nOmniVoice Loaded Successfully!\n")

        return cls._model

    @classmethod
    def generate(
        cls,
        text: str,
        reference_audio: str,
        output_path: str,
        reference_text: str | None = None,
    ):

        model = cls.get_model()

        audio = model.generate(
            text=text,
            ref_audio=reference_audio,
            ref_text=reference_text,
        )

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        sf.write(
            output_path,
            audio[0],
            24000
        )

        return output_path