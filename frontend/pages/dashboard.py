from nicegui import ui

from frontend.components.sidebar import sidebar
from frontend.components.navbar import navbar


@ui.page("/dashboard")
def dashboard():

    sidebar()
    navbar("Dashboard")

    with ui.column().classes("p-8 w-full gap-6"):

        # =====================================================
        # Header
        # =====================================================

        ui.label(
            "Welcome to Mirror Persona AI"
        ).classes(
            "text-4xl font-bold"
        )

        ui.label(
            "Manage your AI persona, generate content and voice, and monitor your progress."
        ).classes(
            "text-gray-500"
        )

        ui.separator()

        # =====================================================
        # Statistics
        # =====================================================

        with ui.row().classes("w-full gap-6"):

            stats = [
                ("📄", "Documents", "1"),
                ("📝", "Generated Texts", "0"),
                ("🎤", "Generated Voices", "0"),
                ("🤖", "Persona Status", "Ready"),
            ]

            for icon, title, value in stats:

                with ui.card().classes(
                    "w-64 h-36 justify-center items-center shadow-md"
                ):

                    ui.label(icon).classes(
                        "text-4xl"
                    )

                    ui.label(title).classes(
                        "text-gray-500"
                    )

                    ui.label(value).classes(
                        "text-3xl font-bold"
                    )

        # =====================================================
        # Quick Actions
        # =====================================================

        ui.label(
            "Quick Actions"
        ).classes(
            "text-2xl font-bold"
        )

        with ui.row().classes("gap-4"):

            ui.button(
                "📄 Upload Document",
                on_click=lambda: ui.navigate.to("/upload")
            ).classes("w-56")

            ui.button(
                "✍ Generate Text",
                on_click=lambda: ui.navigate.to("/generate")
            ).classes("w-56")

            ui.button(
                "🎤 Generate Voice",
                on_click=lambda: ui.navigate.to("/voice")
            ).classes("w-56")

        ui.separator()

        # =====================================================
        # Persona Status
        # =====================================================

        ui.label(
            "Persona Status"
        ).classes(
            "text-2xl font-bold"
        )

        with ui.card().classes("w-full p-5"):

            ui.label("✅ Writing Profile Uploaded")
            ui.label("✅ Voice Profile Uploaded")
            ui.label("✅ AI Ready")

        ui.separator()

        # =====================================================
        # Recent Activity
        # =====================================================

        ui.label(
            "Recent Activity"
        ).classes(
            "text-2xl font-bold"
        )

        with ui.card().classes("w-full p-5"):

            ui.label("📄 No recent document uploads.")
            ui.label("📝 No generated text.")
            ui.label("🎤 No generated voices.")

        ui.separator()

        # =====================================================
        # Footer
        # =====================================================

        ui.label(
            "Mirror Persona AI • Version 1.0"
        ).classes(
            "text-gray-400 text-sm"
        )