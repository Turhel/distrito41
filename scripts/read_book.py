"""Local, read-only reader. Serves only reader assets and the manuscript."""
import argparse
import json
import mimetypes
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import webbrowser

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'reader'
CHAPTERS = ROOT / 'main' / 'caso-001'


class ReaderHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = unquote(urlsplit(self.path).path)
        if route == '/book.json':
            chapters = []
            for path in sorted(CHAPTERS.glob('[0-9][0-9]-*.md')):
                text = path.read_text(encoding='utf-8')
                lines = text.splitlines()
                chapters.append({'id': path.stem, 'title': lines[0], 'lines': lines[1:]})
            body = json.dumps(chapters, ensure_ascii=False).encode('utf-8')
            self.respond(body, 'application/json; charset=utf-8')
            return
        relative = route.lstrip('/') or 'index.html'
        path = (ASSETS / relative).resolve()
        if not path.is_relative_to(ASSETS.resolve()) or not path.is_file():
            self.send_error(404)
            return
        mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
        self.respond(path.read_bytes(), mime)

    def respond(self, body, mime):
        self.send_response(200)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write(body)


def main():
    parser = argparse.ArgumentParser(description='Leitor local do Distrito 41')
    parser.add_argument('--port', type=int, default=8041)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), ReaderHandler)
    url = f'http://127.0.0.1:{server.server_port}'
    print(f'Distrito 41: {url} (Ctrl+C para encerrar)', flush=True)
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
