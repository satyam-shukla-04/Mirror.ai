import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from backend.services.omnivoice_service import OmniVoiceService

print("First")
OmniVoiceService.get_model()

print("Second")
OmniVoiceService.get_model()

print("Done")