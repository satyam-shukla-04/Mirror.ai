from nicegui import ui
from frontend.utils.generation import get_generated_text_id
from components.sidebar import sidebar
from components.navbar import navbar

from frontend.services.voice_service import generate_voice
from frontend.services.api import BASE_URL
from frontend.utils.generation import get_generated_text_id
@ui.page("/voice")
def voice_page():

    sidebar()
    navbar("Voice Generation")

    with ui.column().classes("p-8 w-full gap-4"):

        ui.label("Generate Voice").classes(
            "text-3xl font-bold"
        )

        ui.label(
            "Generate speech using your cloned voice."
        ).classes(
            "text-gray-500"
        )

        prompt = ui.textarea(
            label="Enter Text"
        ).props(
            "outlined"
        ).classes(
            "w-full"
        )

        audio_player = ui.audio("").classes("w-full")

        download_link = ui.link(
            "⬇ Download Voice",
            "#"
        )

        download_link.visible = False

        async def handle_generate():

            generated_text_id = get_generated_text_id()

            print("Generated Text ID:", generated_text_id)

            if generated_text_id is None:

                ui.notify(
                    "Please generate text first.",
                    color="warning"
                )
                return

            ui.notify(
                "Generating voice...",
                color="primary"
            )

            response = generate_voice(
                generated_text_id
            )

            if response.status_code != 200:

                try:
                    ui.notify(
                        response.json()["detail"],
                        color="negative"
                    )
                except Exception:
                    ui.notify(
                        response.text,
                        color="negative"
                    )

                return

            data = response.json()

            audio_url = BASE_URL + data["audio_path"]

            # NiceGUI 3.13
            audio_player.props(f'src="{audio_url}"')
            audio_player.update()

            download_link.set_text("⬇ Download Voice")
            download_link.set_target(audio_url)
            download_link.visible = True

            ui.notify(
                "Voice generated successfully!",
                color="positive"
            )

        with ui.row():

            ui.button(
                "Generate Voice",
                icon="graphic_eq",
                on_click=handle_generate
            )

            ui.button(
                "Clear",
                icon="delete",
                on_click=lambda: (
                    prompt.set_value(""),
                    audio_player.props('src=""'),
                    audio_player.update(),
                    setattr(download_link, "visible", False)
                )
            )