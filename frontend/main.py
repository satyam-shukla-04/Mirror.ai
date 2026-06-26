import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))

from nicegui import ui
import pages.login
import pages.register
import pages.dashboard
import pages.upload
import pages.analysis
import pages.generate
import pages.voice
import pages.evalution
ui.run(reload=True)