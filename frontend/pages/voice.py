from nicegui import ui

from components.sidebar import sidebar
from components.navbar import navbar

from frontend.services.api import BASE_URL
from frontend.services.voice_service import (
    generate_voice,
    get_voice_history,
)
from frontend.utils.generation import get_generated_text_id


@ui.page("/voice")
def voice_page():

    sidebar()
    navbar("Voice Generation")

    with ui.column().classes("p-8 w-full gap-4"):

        ui.label("Voice Generation").classes(
            "text-3xl font-bold"
        )

        ui.label(
        "Generate speech using your cloned voice."
        ).classes(
         "text-gray-500"
        )

        voice_source = ui.radio(
            {
                "generated": "Use Generated Text",
                "custom": "Enter Custom Text",
            },
            value="generated",
        ).props("inline")

        generated_container = ui.column().classes("w-full")
        custom_container = ui.column().classes("w-full")



        # -------------------------
        # Voice Source
        # -------------------------

        voice_source = ui.radio(
            {
                "generated": "Use Generated Text",
                "custom": "Enter Custom Text",
            },
            value="generated",
        ).classes("mb-4")

    with generated_container:

        ui.label(
            "Latest generated text will be used."
        ).classes(
            "text-gray-500"
        )

    with custom_container:

        custom_text = ui.textarea(
            label="Custom Text",
            placeholder="Type anything you want your cloned voice to speak..."
        ).classes("w-full")

        def update_source():

            generated_container.visible = (
                voice_source.value == "generated"
            )

            custom_container.visible = (
                voice_source.value == "custom"
            )


        voice_source.on(
            "update:model-value",
            lambda _: update_source()
        )

        update_source()
        # -------------------------
        # Current Generated Voice
        # -------------------------

        ui.label("Current Voice").classes(
            "text-xl font-bold mt-4"
        )

        audio_player = ui.audio("").classes("w-full")

        download_link = ui.link(
            "⬇ Download Voice",
            "#"
        )

        download_link.visible = False

        # -------------------------
        # Voice History Container
        # -------------------------

        history_column = ui.column().classes("w-full mt-8")

        # -------------------------
        # Load Voice History
        # -------------------------

        def load_history():

            history_column.clear()

            response = get_voice_history()

            if response.status_code != 200:
                return

            voices = response.json()

            with history_column:

                ui.separator()

                ui.label(
                    "Voice History"
                ).classes(
                    "text-2xl font-bold"
                )

                if not voices:

                    ui.label(
                        "No generated voices yet."
                    ).classes(
                        "text-gray-500"
                    )

                    return

                for voice in voices:

                    audio_url = BASE_URL + voice["audio_path"]

                    with ui.card().classes("w-full"):

                        ui.label(
                            f"Generated At: {voice['created_at']}"
                        ).classes(
                            "font-semibold"
                        )

                        if voice.get("prompt"):
                            ui.label(
                                f"Prompt: {voice['prompt']}"
                            )

                        ui.audio(audio_url).classes("w-full")

                        ui.link(
                            "⬇ Download",
                            audio_url,
                        )

        # Load history when page opens
        load_history()

        # -------------------------
        # Generate Voice
        # -------------------------

        async def handle_generate():

            ui.notify(
                "Generating voice...",
                color="primary",
            )

            if voice_source.value == "generated":

                generated_text_id = get_generated_text_id()

                if generated_text_id is None:

                    ui.notify(
                        "Please generate text first.",
                        color="warning",
                    )

                    return

                response = generate_voice(
                    generated_text_id=generated_text_id
                )

            else:

                if not custom_text.value.strip():

                    ui.notify(
                        "Please enter some text.",
                        color="warning",
                    )

                    return

                response = generate_voice(
                    custom_text=custom_text.value
                )

            if response.status_code != 200:

                try:

                    ui.notify(
                        response.json()["detail"],
                        color="negative",
                    )

                except Exception:

                    ui.notify(
                        response.text,
                        color="negative",
                    )

                return

            data = response.json()

            audio_url = BASE_URL + data["audio_path"]

            audio_player.props(
                f'src="{audio_url}"'
            )

            audio_player.update()

            download_link.set_target(audio_url)
            download_link.visible = True

            load_history()

            ui.notify(
                "Voice generated successfully!",
                color="positive",
            )       

        # -------------------------
        # Buttons
        # -------------------------

        with ui.row():

            ui.button(
                "Generate Voice",
                icon="graphic_eq",
                on_click=handle_generate,
            )

            ui.button(
                "Refresh History",
                icon="refresh",
                on_click=load_history,
            )

            ui.button(
                "Clear",
                icon="delete",
                on_click=lambda: (
                    audio_player.props('src=""'),
                    audio_player.update(),
                    setattr(download_link, "visible", False),
                ),
            )