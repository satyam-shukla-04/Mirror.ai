from nicegui import ui


def sidebar():

    with ui.left_drawer(top_corner=True, bottom_corner=True).style(
        'background:#111827'
    ):

        ui.label('Mirror AI').classes(
            'text-2xl font-bold text-white p-4'
        )

        ui.separator()
        with ui.link(target='/dashboard'):
            ui.button("Dashboard", icon="dashboard")
        #ui.button("Dashboard", icon="dashboard")

        
        with ui.link(target='/upload'):
            ui.button("Upload", icon="upload")
        
        with ui.link(target='/analysis'):
            ui.button("Analytics", icon="analytics")
        with ui.link(target='/generate'):
            ui.button("Generate", icon="edit")
        with ui.link(target='/voice'):
            ui.button("Voice", icon="mic")   
        with ui.link(target='/evaluation'):
            ui.button("Evaluation", icon="grading")
        
        """ui.button(
    'Dashboard',
    on_click=lambda: ui.navigate.to('/dashboard')
).props('flat').classes('w-full justify-start text-white')
"""
        #ui.link('Upload', '/upload').classes('text-white p-2')
        #ui.link('Generate Text', '/generate').classes('text-white p-2')
        #ui.link('Voice Generation', '/voice').classes('text-white p-2')
        #ui.link('Evaluation', '/evaluation').classes('text-white p-2')