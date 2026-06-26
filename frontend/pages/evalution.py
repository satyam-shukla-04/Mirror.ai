from nicegui import ui
import json
from backend.services.evaluation import evaluate_persona

from components.sidebar import sidebar
from components.navbar import navbar


@ui.page("/evaluation")
def evaluation_page():

    sidebar()
    navbar("Persona Evaluation")

    report = evaluate_persona()

    with ui.column().classes("p-8 w-full gap-6"):

        ui.label("Mirror Persona Evaluation").classes(
            "text-3xl font-bold"
        )

        ui.label(
            "Check whether your writing and voice persona are ready."
        ).classes(
            "text-gray-500"
        )

        # -----------------------------
        # Upload Status
        # -----------------------------

        with ui.card().classes("w-full p-4"):

            ui.label("Upload Status").classes(
                "text-xl font-bold"
            )

            ui.label(
                f"Writing Reference : {'✅ Uploaded' if report['writing_reference'] else '❌ Missing'}"
            )

            ui.label(
                f"Voice Reference : {'✅ Uploaded' if report['voice_reference'] else '❌ Missing'}"
            )

            ui.label(
                f"Style Profile : {'✅ Generated' if report['style_profile'] else '❌ Missing'}"
            )

            ui.label(
                f"Voice Profile : {'✅ Generated' if report['voice_profile'] else '❌ Missing'}"
            )

        # -----------------------------
        # Writing Profile
        # -----------------------------

        if report["style"]:

            style = report["style"]
            if isinstance(style, str):
                style = json.loads(style)

            with ui.card().classes("w-full p-4"):

                ui.label("Writing Style").classes(
                    "text-xl font-bold"
                )

                ui.label(f"Tone : {style.get('tone', 'N/A')}")

                ui.label(f"Formality : {style.get('formality', 'N/A')}")

                ui.label(f"Directness : {style.get('directness', 'N/A')}")

                ui.label(f"Verbosity : {style.get('verbosity', 'N/A')}")

                ui.label(f"Technicality : {style.get('technicality', 'N/A')}")

                patterns = style.get("writing_patterns", [])

                if patterns:

                    ui.label("Writing Patterns").classes(
                        "font-bold mt-2"
                    )

                    for pattern in patterns:

                        ui.label(f"• {pattern}")

        # -----------------------------
        # Voice Profile
        # -----------------------------

        if report["voice"]:

            voice = report["voice"]
            if isinstance(style, str):
                style = json.loads(style)

            with ui.card().classes("w-full p-4"):

                ui.label("Voice Profile").classes(
                    "text-xl font-bold"
                )

                ui.label(
                    f"Duration : {voice.get('duration', 'N/A')} sec"
                )

                ui.label(
                    f"Sample Rate : {voice.get('sample_rate', 'N/A')} Hz"
                )

                ui.label(
                    f"Channels : {voice.get('channels', 'N/A')}"
                )

                ui.label(
                    f"Format : {voice.get('format', 'N/A')}"
                )

                ui.label(
                    f"Average Pitch : {voice.get('average_pitch_hz', 'N/A')} Hz"
                )

                ui.label(
                    f"Average Volume : {voice.get('average_volume', 'N/A')}"
                )

                ui.label(
                    f"Silence Ratio : {voice.get('silence_ratio', 'N/A')}"
                )

        # -----------------------------
        # Overall Status
        # -----------------------------

        with ui.card().classes("w-full p-4"):

            ui.label("Overall Status").classes(
                "text-xl font-bold"
            )

            if report["persona_ready"]:

                ui.label(
                    "🟢 Persona Ready"
                ).classes(
                    "text-green text-2xl font-bold"
                )

                ui.label(
                    "Mirror AI has successfully learned your writing and voice profile."
                )

            else:

                ui.label(
                    "🔴 Persona Incomplete"
                ).classes(
                    "text-red text-2xl font-bold"
                )

                ui.label(
                    "Please upload both a writing reference and a voice reference."
                )