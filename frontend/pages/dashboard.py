from nicegui import ui
from components.sidebar import sidebar
from components.navbar import navbar

@ui.page('/dashboard')
def dashboard():

    sidebar()
    navbar('Dashboard')

    with ui.column().classes('p-8 w-full'):

        ui.label(
            'Welcome to Mirror AI'
        ).classes('text-3xl font-bold')

        with ui.row():

            for title, value in [
                ('Documents', '24'),
                ('Audio Files', '12'),
                ('Profile Strength', '85%'),
                ('Similarity Score', '82%')
            ]:

                with ui.card().classes(
                    'w-64 h-32'
                ):
                    ui.label(title)
                    ui.label(value).classes(
                        'text-3xl font-bold'
                    )