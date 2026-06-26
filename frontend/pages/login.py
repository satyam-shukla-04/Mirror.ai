from nicegui import ui

@ui.page('/')
def login():

    with ui.column().classes(
        'absolute-center items-center w-96'
    ):

        ui.label('Mirror AI').classes(
            'text-4xl font-bold'
        )

        ui.label(
            'AI Personality & Communication Cloning'
        )

        ui.input('Email').classes('w-full')

        ui.input(
            'Password',
            password=True
        ).classes('w-full')

        ui.button(
            'Login',
            on_click=lambda: ui.navigate.to('/dashboard')
        ).classes('w-full')

        ui.link(
            'Create Account',
            '/register'
        )