"""
Valentine Builder & Server
──────────────────────────
• Reads per-theme messages from messages.py
• Injects them into template.html → dist/index.html
• Serves on localhost:8080
"""

import json, os, sys, http.server, socketserver, webbrowser
from pathlib import Path
from datetime import datetime
from messages import MESSAGES, YES_RESPONSES

ROOT     = Path(__file__).parent
TEMPLATE = ROOT / "template.html"
DIST     = ROOT / "dist"
OUTPUT   = DIST / "index.html"
PORT     = 8080


def build():
    print("🔨 Building…")
    assert TEMPLATE.exists(), f"Missing {TEMPLATE}"
    DIST.mkdir(exist_ok=True)

    html = TEMPLATE.read_text("utf-8")

    blob = f"""
    <!-- Injected by build.py @ {datetime.now().strftime('%H:%M:%S')} -->
    <script>
    window.__V__ = {{
      msgs: {json.dumps(MESSAGES, ensure_ascii=False)},
      yes:  {json.dumps(YES_RESPONSES, ensure_ascii=False)},
    }};
    </script>"""

    html = html.replace("</head>", blob + "\n</head>")
    OUTPUT.write_text(html, "utf-8")
    print(f"✅ Built → {OUTPUT}")


def serve():
    os.chdir(DIST)
    h = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), h) as s:
        url = f"http://localhost:{PORT}"
        print(f"💕 Serving at {url}")
        try: webbrowser.open(url)
        except: pass
        try: s.serve_forever()
        except KeyboardInterrupt: print("\n👋 Bye!")


if __name__ == "__main__":
    build()
    if "--build-only" not in sys.argv:
        serve()
