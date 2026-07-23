from pathlib import Path
import requests
from frontend.services.api import BASE_URL, get_headers
from nicegui import ui
from frontend.services.upload_service import (
    upload_document,
    upload_voice,
)
from frontend.services.upload_service import upload_document

from components.sidebar import sidebar
from components.navbar import navbar


@ui.page("/upload")
def upload_page():

    sidebar()
    navbar("Upload Center")

    def on_upload(event):

        temp_path = Path("temp_upload")
        temp_path.mkdir(exist_ok=True)

        file_path = temp_path / event.file.name

        with open(file_path, "wb") as f:
            f.write(event.file._data)

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

    with ui.column().classes("p-8"):

        ui.label(
           "Upload Writing Sample"
        ).classes(
             "text-2xl font-bold"
        )

        ui.upload(
            on_upload=on_upload,
            auto_upload=True
        ).classes("w-96")

        ui.separator()

        ui.label(
                "Upload Voice Sample"
        ).classes(
                "text-2xl font-bold"
            )

        ui.upload(
        on_upload=on_voice_upload,
        auto_upload=True
        ).props(
            "accept=.wav,.mp3,.m4a"
            ).classes("w-96").classes("w-96")

def upload_voice(file_path: str):
    with open(file_path, "rb") as f:
        return requests.post(
            f"{BASE_URL}/upload/voice",
            headers=get_headers(),
            files={
                "file": f
            }
        )
    
def on_voice_upload(event):

    temp_path = Path("temp_upload")
    temp_path.mkdir(exist_ok=True)

    file_path = temp_path / event.file.name

    with open(file_path, "wb") as f:
        f.write(event.file._data)

    response = upload_voice(str(file_path))

    if response.status_code == 200:
        ui.notify(
            "Voice uploaded successfully!",
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