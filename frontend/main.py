import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))

from nicegui import ui
import pages.login
import pages.register
import pages.dashboard
try:
    import pages.upload
    print("✅ upload loaded")
except Exception as e:
    print("❌ upload", e)

try:
    import pages.analysis
    print("✅ analysis loaded")
except Exception as e:
    print("❌ analysis", e)

try:
    import pages.generate
    print("✅ generate loaded")
except Exception as e:
    print("❌ generate", e)

try:
    import pages.voice
    print("✅ voice loaded")
except Exception as e:
    print("❌ voice", e)

try:
    import pages.evalution
    print("✅ evaluation loaded")
except Exception as e:
    print("❌ evaluation", e)
ui.run()