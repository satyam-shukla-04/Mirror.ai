from nicegui import ui

def navbar(title):

    with ui.header().classes(
        'bg-slate-900 text-white'
    ):
        ui.label(title).classes(
            'text-xl font-bold'
        )