
from nicegui import ui

# Import core pages
import frontend.pages.login
import frontend.pages.register
import frontend.pages.dashboard


# Import remaining pages and show any import errors
def load_page(module_name: str, page_name: str) -> None:
    try:
        __import__(module_name)
        print(f"✅ {page_name} page loaded")
    except Exception as e:
        print(f"❌ Failed to load {page_name} page: {e}")
        raise


load_page("frontend.pages.upload", "Upload")
load_page("frontend.pages.analysis", "Analysis")
load_page("frontend.pages.generate", "Generate")
load_page("frontend.pages.voice", "Voice")
load_page("frontend.pages.evalution", "Evaluation")


# Start NiceGUI
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        host="127.0.0.1",
        port=8080,
        reload=False,
        title="Mirror Persona AI",
    )
