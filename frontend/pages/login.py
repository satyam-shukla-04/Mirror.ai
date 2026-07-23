from nicegui import ui

from frontend.services.auth_service import login


@ui.page("/")
def login_page():

    with ui.column().classes(
        "absolute-center items-center w-96"
    ):

        ui.label("Mirror AI").classes(
            "text-4xl font-bold"
        )

        ui.label(
            "AI Personality & Communication Cloning"
        )

        email = ui.input(
            "Email"
        ).classes("w-full")

        password = ui.input(
            "Password",
            password=True,
            password_toggle_button=True
        ).classes("w-full")

        def login_user():

            if not email.value or not password.value:
                ui.notify(
                    "Please enter email and password.",
                    color="negative"
                )
                return

            result = login(
                email.value,
                password.value
            )

            if result is None:
                ui.notify(
                    "Invalid email or password.",
                    color="negative"
                )
                return

            ui.notify(
                "Login successful!",
                color="positive"
            )

            ui.navigate.to("/dashboard")

        ui.button(
            "Login",
            on_click=login_user
        ).classes("w-full")

        ui.link(
            "Create Account",
            "/register"
        )