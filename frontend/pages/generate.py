from nicegui import ui

from components.sidebar import sidebar
from components.navbar import navbar

from backend.services.text_generator import generate_text


@ui.page('/generate')
def generate_page():

    sidebar()
    navbar("Generate Content")

    with ui.column().classes('p-8 w-full'):

        ui.label(
            'Generate Content in Your Style'
        ).classes(
            'text-3xl font-bold'
        )

        ui.label(
            'Enter a prompt and Mirror AI will generate content using your saved writing style.'
        ).classes(
            'text-gray-500'
        )

        prompt_input = ui.textarea(
            label='Enter Prompt'
        ).props(
            'outlined'
        ).classes(
            'w-full'
        )

        output_box = ui.textarea(
            label='Generated Content'
        ).props(
            'outlined readonly'
        ).classes(
            'w-full'
        )

        async def handle_generate():

            if not prompt_input.value:

                ui.notify(
                    'Please enter a prompt',
                    type='warning'
                )

                return

            output_box.set_value(
                'Generating content...'
            )

            try:

                result = generate_text(
                    prompt_input.value
                )

                output_box.set_value(
                    result
                )

                ui.notify(
                    'Content generated successfully',
                    type='positive'
                )

            except Exception as e:

                output_box.set_value('')

                ui.notify(
                    f'Error: {str(e)}',
                    type='negative'
                )

        with ui.row():

            ui.button(
                'Generate',
                icon='auto_awesome',
                on_click=handle_generate
            )

            ui.button(
                'Clear',
                icon='delete',
                on_click=lambda: (
                    prompt_input.set_value(''),
                    output_box.set_value('')
                )
            )