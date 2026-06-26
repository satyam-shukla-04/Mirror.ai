from nicegui import ui
from components.sidebar import sidebar
from components.navbar import navbar

@ui.page('/voice')
def voice():

    sidebar()
    navbar('Voice Generation')

    with ui.column().classes('p-8'):

        ui.textarea(
            label='Prompt'
        ).classes('w-full')

        ui.button('Generate Voice')

        ui.audio(
            'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
        )