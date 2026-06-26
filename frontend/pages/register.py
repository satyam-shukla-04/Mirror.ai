from nicegui import ui

@ui.page('/register')
def register():

    with ui.column().classes(
        'absolute-center items-center w-96'
    ):

        ui.label('Create Account').classes(
            'text-3xl font-bold'
        )

        ui.input('Full Name').classes('w-full')

        ui.input('Email').classes('w-full')

        ui.input(
            'Password',
            password=True
        ).classes('w-full')

        ui.input(
            'Confirm Password',
            password=True
        ).classes('w-full')

        ui.button(
            'Register'
        ).classes('w-full')