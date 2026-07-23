from nicegui import ui

from components.sidebar import sidebar
from components.navbar import navbar

from frontend.services.evaluation_service import evaluate_text
from frontend.utils.generation import get_generated_text_id


@ui.page("/evaluation")
def evaluation_page():

    sidebar()
    navbar("Evaluation")

    with ui.column().classes("p-8 w-full gap-6"):

        ui.label(
            "Mirror AI Evaluation"
        ).classes(
            "text-3xl font-bold"
        )

        ui.label(
            "Evaluate how closely the generated text matches your writing style."
        ).classes(
            "text-gray-500"
        )

        score_label = ui.label("").classes(
            "text-5xl font-bold text-blue"
        )

        metrics = ui.column().classes("gap-2")

        strengths = ui.column().classes("gap-1")

        weaknesses = ui.column().classes("gap-1")

        suggestions = ui.column().classes("gap-1")

        def run_evaluation():

            generated_text_id = get_generated_text_id()

            if generated_text_id is None:

                ui.notify(
                    "Generate some text first.",
                    color="warning"
                )

                return

            response = evaluate_text(
                generated_text_id
            )

            if not response.ok:

                ui.notify(
                    "Evaluation failed.",
                    color="negative"
                )

                return

            data = response.json()["evaluation"]

            score_label.set_text(
                f"{data['overall_score']} / 100"
            )

            metrics.clear()

            strengths.clear()

            weaknesses.clear()

            suggestions.clear()

            with metrics:

                ui.label(f"Tone : {data['tone']}")

                ui.label(f"Vocabulary : {data['vocabulary']}")

                ui.label(f"Sentence Structure : {data['sentence_structure']}")

                ui.label(f"Paragraph Flow : {data['paragraph_flow']}")

                ui.label(f"Writing Habits : {data['writing_habits']}")

                ui.label(f"Human Likeness : {data['human_likeness']}")

            with strengths:

                ui.label("Strengths").classes(
                    "text-xl font-bold"
                )

                for item in data["strengths"]:

                    ui.label(f"✓ {item}")

            with weaknesses:

                ui.label("Weaknesses").classes(
                    "text-xl font-bold"
                )

                for item in data["weaknesses"]:

                    ui.label(f"✗ {item}")

            with suggestions:

                ui.label("Suggestions").classes(
                    "text-xl font-bold"
                )

                for item in data["suggestions"]:

                    ui.label(f"• {item}")

            ui.notify(
                "Evaluation completed.",
                color="positive"
            )

        ui.button(
            "Evaluate",
            icon="analytics",
            on_click=run_evaluation
        )