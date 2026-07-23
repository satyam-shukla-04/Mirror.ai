from nicegui import ui

from frontend.services.auth_service import register


@ui.page('/register')
def register_page():

     with ui.column().classes(
        'absolute-center items-center w-96'
    ):

        ui.label('Create Account').classes(
            'text-3xl font-bold'
        )

        username = ui.input(
            'Full Name'
        ).classes('w-full')

        email = ui.input(
            'Email'
        ).classes('w-full')

        password = ui.input(
            'Password',
            password=True,
            password_toggle_button=True
        ).classes('w-full')

        confirm_password = ui.input(
            'Confirm Password',
            password=True,
            password_toggle_button=True
        ).classes('w-full')

        def register_user():

            if (
                not username.value or
                not email.value or
                not password.value or
                not confirm_password.value
            ):
                ui.notify(
                    'Please fill all fields.',
                    color='negative'
                )
                return

            if password.value != confirm_password.value:
                ui.notify(
                    'Passwords do not match.',
                    color='negative'
                )
                return

            response = register(
                username.value,
                email.value,
                password.value
            )

            if response.status_code == 200  :
                ui.notify(
                    'Registration successful!',
                    color='positive'
                )

                ui.navigate.to('/')

            else:
                try:
                    error = response.json()
                    message = error.get(
                        "detail",
                        "Registration failed."
                    )
                except Exception:
                    message = "Registration failed."

                ui.notify(
                    message,
                    color='negative'
                )

        ui.button(
            'Register',
            on_click=register_user
        ).classes('w-full')

        ui.link(
            'Already have an account?',
            '/'
        )