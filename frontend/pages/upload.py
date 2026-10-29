from pathlib import Path
import shutil

from nicegui import ui

from frontend.services.upload_service import (
    upload_document,
    upload_voice,
)

from frontend.components.sidebar import sidebar
from frontend.components.navbar import navbar


def on_document_upload(event):

    temp_path = Path("temp_upload")
    temp_path.mkdir(exist_ok=True)

    file_path = temp_path / event.file.name

    if hasattr(event.file, "_path"):
        # LargeFileUpload
        shutil.copy(event.file._path, file_path)
    else:
        # SmallFileUpload
        with open(file_path, "wb") as f:
            f.write(event.file._data)
        shutil.copy(event.file._path, file_path)

    response = upload_document(str(file_path))

    if response.status_code == 200:
        ui.notify(
            "Document uploaded successfully!",
            color="positive"
        )
    else:
        try:
            message = response.json()["detail"]
        except Exception:
            message = response.text

        ui.notify(
            message,
            color="negative"
        )

def on_voice_upload(event):

    temp_path = Path("temp_upload")
    temp_path.mkdir(exist_ok=True)

    file_path = temp_path / event.file.name

    # Works for both SmallFileUpload and LargeFileUpload
    if hasattr(event.file, "_path"):
        shutil.copy(event.file._path, file_path)
    else:
        with open(file_path, "wb") as f:
            f.write(event.file._data)

    response = upload_voice(str(file_path))

    if response.status_code == 200:
        ui.notify("Voice uploaded successfully!", color="positive")
    else:
        try:
            ui.notify(response.json()["detail"], color="negative")
        except Exception:
            ui.notify(response.text, color="negative")


            
@ui.page("/upload")
def upload_page():

    sidebar()
    navbar("Upload Center")

    with ui.column().classes("p-8 gap-6"):

        ui.label(
            "Upload Writing Sample"
        ).classes(
            "text-2xl font-bold"
        )

        ui.upload(
            on_upload=on_document_upload,
            auto_upload=True,
        ).props(
            "accept=.pdf,.doc,.docx,.txt"
        ).classes(
            "w-96"
        )

        ui.separator()

        ui.label(
            "Upload Voice Sample"
        ).classes(
            "text-2xl font-bold"
        )

        ui.upload(
            on_upload=on_voice_upload,
            auto_upload=True,
        ).props(
            "accept=.wav,.mp3,.m4a"
        ).classes(
            "w-96"
        )

