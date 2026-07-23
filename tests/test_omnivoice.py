from pathlib import Path
import soundfile as sf
import torch
from omnivoice import OmniVoice

BASE_DIR = Path(__file__).resolve().parent.parent

voice_path = BASE_DIR / "uploads" / "audio" / "voice_reference.wav"

print("Reference audio:", voice_path)
print("Exists:", voice_path.exists())

model = OmniVoice.from_pretrained(
    "k2-fsa/OmniVoice",
    device_map="cpu",          # We'll use CPU for now
    dtype=torch.float32,
)

audio = model.generate(
    text="Hello everyone. Welcome to Mirror AI. This is my cloned voice.",
    ref_audio=str(voice_path),
)

output_path = BASE_DIR / "output.wav"

sf.write(
    str(output_path),
    audio[0],
    24000
)

print("Done!")
print("Output saved at:", output_path)