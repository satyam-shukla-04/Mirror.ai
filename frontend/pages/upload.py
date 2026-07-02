import json
from pathlib import Path
from nicegui import ui
from backend.services.document_parser import extract_text
from backend.services.text_storage import save_extracted_text
from backend.services.style_analyzer import analyze_style
from backend.services.profile_storage import save_profile
from backend.services.groq_style_analyzer import (analyze_style_with_groq)
from components.sidebar import sidebar
from components.navbar import navbar
from backend.services.voice_analyzer import analyze_voice
from backend.services.voice_storage import save_voice_profile

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DOCUMENTS_DIR = BASE_DIR / 'uploads' / 'documents'
AUDIO_DIR = BASE_DIR / 'uploads' / 'audio'

DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
print("Documents:", DOCUMENTS_DIR)
print("Audio:", AUDIO_DIR)

from backend.services.upload_service import process_document

async def save_document(e):

    content = await e.file.read()

    result = process_document(
        e.file.name,
        content
    )

    ui.notify(
        result["message"],
        type="positive"
    )
async def save_audio(e):

    extension = Path(e.file.name).suffix

    file_path = AUDIO_DIR / f"voice_reference{extension}"

    await e.file.save(file_path)
    profile = analyze_voice(str(file_path))
    save_voice_profile(profile)
    

    print(f"Saved: {file_path}")

    ui.notify(
        f"Audio uploaded: {e.file.name}",
        type="positive"
    )
@ui.page('/upload')
def upload_page():

    sidebar()
    navbar("Upload Center")

    with ui.column().classes('p-8'):

        ui.label('Upload Documents').classes(
            'text-2xl font-bold'
        )

        ui.upload(
            on_upload=save_document
        )

        ui.separator()

        ui.label('Upload Audio').classes(
            'text-2xl font-bold'
        )

        ui.upload(
            on_upload=save_audio
        )