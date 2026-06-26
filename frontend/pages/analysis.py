from nicegui import ui
from components.sidebar import sidebar
from components.navbar import navbar

@ui.page('/analysis')
def analysis():

    sidebar()
    navbar('Style Analysis')

    option = {
        'radar': {
            'indicator': [
                {'name': 'Formality', 'max': 100},
                {'name': 'Directness', 'max': 100},
                {'name': 'Humor', 'max': 100},
                {'name': 'Positivity', 'max': 100},
                {'name': 'Verbosity', 'max': 100},
                {'name': 'Technicality', 'max': 100},
            ]
        },
        'series': [{
            'type': 'radar',
            'data': [{
                'value': [85,90,35,75,60,80]
            }]
        }]
    }

    sidebar()
    ui.echart(option).classes('w-full h-96')