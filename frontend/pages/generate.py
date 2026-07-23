from nicegui import ui

from components.sidebar import sidebar
from components.navbar import navbar

from frontend.services.generate_service import generate_text
from frontend.services.voice_service import generate_voice
from frontend.services.api import BASE_URL

from frontend.utils.generation import (
    save_generated_text_id,
    get_generated_text_id
)


@ui.page("/generate")
def generate_page():

    sidebar()
    navbar("Mirror AI Studio")

    with ui.column().classes("p-8 w-full gap-5"):

        ui.label(
            "Mirror AI Studio"
        ).classes(
            "text-3xl font-bold"
        )

        ui.label(
            "Generate personalized content in your own writing style and instantly convert it into your cloned voice."
        ).classes(
            "text-gray-500"
        )

        prompt_input = ui.textarea(
            label="Enter Prompt"
        ).props(
            "outlined"
        ).classes(
            "w-full h-40"
        )

        output_box = ui.textarea(
            label="Generated Content"
        ).props(
            "outlined readonly autogrow"
        ).classes(
            "w-full min-h-[400px]"
        )

        audio_player = ui.audio("").classes("w-full")

        download_link = ui.link(
            "⬇ Download Voice",
            "#"
        )

        download_link.visible = False

        # --------------------------
        # Generate Text
        # --------------------------

        def handle_generate():

            if not prompt_input.value:

                ui.notify(
                    "Please enter a prompt.",
                    color="warning"
                )
                return

            generate_button.disable()

            output_box.set_value(
                "Generating content..."
            )

            try:

                response = generate_text(
                    prompt_input.value
                )

                if response.status_code == 200:

                    data = response.json()
                    print(data)

                    save_generated_text_id(
                        data["generated_text_id"]
                    )

                    output_box.set_value(
                        data["generated_text"]
                    )

                    ui.notify(
                        "Content generated successfully.",
                        color="positive"
                    )

                else:

                    try:
                        message = response.json()["detail"]
                    except Exception:
                        message = response.text

                    output_box.set_value("")

                    ui.notify(
                        message,
                        color="negative"
                    )

            except Exception as e:

                output_box.set_value("")

                ui.notify(
                    str(e),
                    color="negative"
                )

            finally:

                generate_button.enable()

        # --------------------------
        # Generate Voice
        # --------------------------

        def handle_generate_voice():

            generated_text_id = get_generated_text_id()
            print("Generated Text ID:", generated_text_id)

            if generated_text_id is None:

                ui.notify(
                    "Generate text first.",
                    color="warning"
                )
                return

            voice_button.disable()

            try:

                response = generate_voice(
                    generated_text_id
                )

                if response.status_code == 200:

                    data = response.json()

                    audio_url = BASE_URL + data["audio_path"]

                    audio_player.set_source(
                        audio_url
                    )

                    download_link.set_target(
                        audio_url
                    )

                    download_link.visible = True

                    ui.notify(
                        "Voice generated successfully.",
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

            except Exception as e:

                ui.notify(
                    str(e),
                    color="negative"
                )

            finally:

                voice_button.enable()

        # --------------------------
        # Buttons
        # --------------------------

        with ui.row().classes("gap-3"):

            generate_button = ui.button(
                "Generate",
                icon="auto_awesome",
                on_click=handle_generate
            )

            voice_button = ui.button(
                "Generate Voice",
                icon="graphic_eq",
                on_click=handle_generate_voice
            )

            ui.button(
                "Copy",
                icon="content_copy",
                on_click=lambda: ui.run_javascript(
                    f'navigator.clipboard.writeText({repr(output_box.value)})'
                )
            )

            ui.button(
                "Clear",
                icon="delete",
                on_click=lambda: (
                    prompt_input.set_value(""),
                    output_box.set_value(""),
                    audio_player.set_source(""),
                    setattr(download_link, "visible", False)
                )
            )
            