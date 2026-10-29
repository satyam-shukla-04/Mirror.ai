from nicegui import ui

from frontend.components.sidebar import sidebar
from frontend.components.navbar import navbar

from frontend.services.api import BASE_URL
from frontend.services.voice_service import (
    generate_voice,
    get_voice_history,
    get_reference_voice,
)
from frontend.utils.generation import get_generated_text_id


@ui.page("/voice")
def voice_page():

    sidebar()
    navbar("Voice Generation")

    with ui.column().classes("p-8 w-full gap-6"):

        # ======================================================
        # Header
        # ======================================================

        ui.label("Voice Generation").classes(
            "text-3xl font-bold"
        )

        ui.label(
            "Generate natural speech using your cloned voice."
        ).classes(
            "text-gray-500"
        )

        ui.separator()

        # ======================================================
        # Input Card
        # ======================================================

        with ui.card().classes("w-full p-6"):

            ui.label(
                "Enter Custom Text"
            ).classes(
                "text-xl font-semibold"
            )

            ui.label(
                "Leave this empty to automatically use your latest generated text."
            ).classes(
                "text-gray-500 text-sm"
            )

            custom_text = ui.textarea(
                placeholder="Type anything you want your cloned voice to speak..."
            ).classes("w-full")

            ui.separator()

            ui.label(
                "Latest Generated Text"
            ).classes(
                "text-lg font-semibold"
            )

            latest_text = ui.label(
                "Latest generated text will be used automatically if the textbox is empty."
            ).classes(
                "text-gray-600"
            )

        # ======================================================
        # Reference Voice
        # ======================================================

        with ui.card().classes("w-full p-6"):

            ui.label(
                "Reference Voice"
            ).classes(
                "text-xl font-semibold"
            )

            ui.label(
                "This is your uploaded voice profile."
            ).classes(
                "text-gray-500 text-sm"
            )

            reference_player = ui.audio("").classes("w-full")

        # ======================================================
        # Generated Voice
        # ======================================================

        with ui.card().classes("w-full p-6"):

            ui.label(
                "Generated Voice"
            ).classes(
                "text-xl font-semibold"
            )

            generated_player = ui.audio("").classes("w-full")

            download_link = ui.link(
                "⬇ Download Generated Voice",
                "#",
            )

            download_link.visible = False

        # ======================================================
        # Generate Button
        # ======================================================

        generate_btn = ui.button(
            "Generate Voice",
            icon="graphic_eq",
        ).classes(
            "w-52"
        )

        ui.separator()

        # ======================================================
        # History
        # ======================================================

        ui.label(
            "Voice History"
        ).classes(
            "text-2xl font-bold"
        )

        history_column = ui.column().classes(
            "w-full gap-4"
        )

        # ======================================================
        # Helper Functions
        # ======================================================

        def clear_generated():

            generated_player.props('src=""')
            generated_player.update()

            download_link.visible = False
            download_link.update()

        def load_reference_voice():

            try:

                response = get_reference_voice()

                if response.status_code != 200:
                    return

                data = response.json()

                reference_player.props(
                    f'src="{BASE_URL}{data["audio_path"]}"'
                )

                reference_player.update()

            except Exception as e:
                print("Failed to load reference voice:", e)

        def load_history():

            history_column.clear()

            response = get_voice_history()

            if response.status_code != 200:
                return

            voices = response.json()

            with history_column:

                if not voices:

                    ui.label(
                        "No generated voices available."
                    ).classes(
                        "text-gray-500"
                    )

                    return

                for voice in voices:

                    audio_url = BASE_URL + voice["audio_path"]

                    with ui.card().classes("w-full p-4"):

                        ui.label(
                            f"Generated: {voice['created_at']}"
                        ).classes(
                            "font-semibold"
                        )

                        if voice.get("prompt"):

                            ui.label(
                                f"Prompt: {voice['prompt']}"
                            ).classes(
                                "text-gray-500"
                            )

                        ui.audio(audio_url).classes("w-full")

                        ui.link(
                            "⬇ Download",
                            audio_url,
                        )

        async def handle_generate():

            generate_btn.disable()

            ui.notify(
                "Generating voice...",
                color="primary",
            )

            clear_generated()

            if custom_text.value.strip():

                response = generate_voice(
                    custom_text=custom_text.value.strip()
                )

            else:

                generated_text_id = get_generated_text_id()

                if generated_text_id is None:

                    ui.notify(
                        "Generate text first or enter custom text.",
                        color="warning",
                    )

                    generate_btn.enable()
                    return

                response = generate_voice(
                    generated_text_id=generated_text_id
                )

            generate_btn.enable()

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

            generated_player.props(
                f'src="{audio_url}"'
            )

            generated_player.update()

            download_link.set_target(audio_url)

            download_link.visible = True
            download_link.update()

            load_history()

            ui.notify(
                "Voice generated successfully!",
                color="positive",
            )

        # ======================================================
        # Initialize
        # ======================================================

        generate_btn.on_click(handle_generate)

        load_reference_voice()
        load_history()