"""Archive official public War Era queries using GET only (stdlib only)."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPRedirectHandler

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://api2.warera.io/trpc/'
# Full article retrieval counts a view and is intentionally excluded.
ALLOWED = {'country.getAllCountries', 'article.getArticlesPaginated',
           'article.getArticleLiteById', 'event.getEventsPaginated',
           'battle.getBattles', 'battle.getById', 'search.searchAnything', 'region.getRegionsObject', 'user.getUserLite'}


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise RuntimeError('Redirect refused; credentials stay on the official API host.')


def key_from_env():
    key = os.environ.get('WARERA_API_KEY', '')
    if not key and (ROOT / '.env').exists():
        for line in (ROOT / '.env').read_text(encoding='utf-8-sig').splitlines():
            name, sep, value = line.strip().partition('=')
            if sep and name.strip() == 'WARERA_API_KEY':
                key = value.strip().strip('\"\'')
    if not key:
        raise RuntimeError('Set WARERA_API_KEY in .env or the environment.')
    return key


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


class Client:
    def __init__(self, key, output, delay):
        self.key, self.output, self.delay = key, output, delay
        self.opener = build_opener(NoRedirect())
        self.last = 0

    def get(self, endpoint, params):
        if endpoint not in ALLOWED:
            raise RuntimeError('Endpoint is not in the read-only allowlist.')
        url = BASE + endpoint + '?' + urlencode({'input': json.dumps(params, separators=(',', ':'))})
        request = Request(url, headers={'X-API-Key': self.key, 'Accept': 'application/json',
                                       'User-Agent': 'Distrito41Archive/1.0'}, method='GET')
        for attempt in range(5):
            time.sleep(max(0, self.delay - (time.monotonic() - self.last)))
            self.last = time.monotonic()
            try:
                with self.opener.open(request, timeout=45) as response:
                    payload = json.load(response)
                break
            except HTTPError as exc:
                if exc.code not in (429, 500, 502, 503, 504) or attempt == 4:
                    raise RuntimeError(f'{endpoint}: HTTP {exc.code} (response body omitted).') from None
                retry = exc.headers.get('Retry-After', '')
                wait = min(60, float(retry)) if retry.isdigit() else min(30, 2 ** (attempt + 1))
                print(f'HTTP {exc.code}; retry in {wait:g}s.', flush=True)
                time.sleep(wait)
            except URLError:
                raise RuntimeError('Network connection failed; no credentials logged.') from None
        if isinstance(payload, dict) and 'error' in payload:
            raise RuntimeError(f'{endpoint}: API returned an error (body omitted).')
        stamp = datetime.now(timezone.utc).isoformat()
        digest = hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()[:16]
        path = self.output / 'raw' / endpoint / f'{digest}.json'
        save(path, {'collected_at_utc': stamp, 'method': 'GET', 'url': url, 'input': params, 'response': payload})
        result = payload.get('result', {}).get('data', payload) if isinstance(payload, dict) else payload
        if isinstance(result, dict) and 'json' in result:
            result = result['json']
        return result


def paginate(client, endpoint, params, max_pages):
    items, seen = [], set()
    complete = False
    previous_pages = 0
    archive = client.output / (endpoint + '.json')
    if archive.exists():
        previous = json.loads(archive.read_text(encoding='utf-8'))
        if previous.get('filters', params) != params:
            raise RuntimeError('Output folder has different filters; use a new output folder.')
        if previous['complete']:
            return {'records': len(previous['items']), 'complete': True}
        items = previous['items']
        previous_pages = previous['pages']
        params = {**params, 'cursor': previous['next_cursor']}
    for page in range(max_pages):
        data = client.get(endpoint, params)
        if isinstance(data, list):
            rows, cursor = data, None
        elif isinstance(data, dict):
            rows = next((data[k] for k in ('items', 'articles', 'events', 'battles', 'results')
                         if isinstance(data.get(k), list)), None)
            cursor = data.get('nextCursor')
            if rows is None:
                raise RuntimeError(f'Unknown pagination shape for {endpoint}; raw response saved.')
        else:
            raise RuntimeError(f'Unknown response shape for {endpoint}; raw response saved.')
        items.extend(rows)
        save(client.output / (endpoint + '.json'), {'filters': {k: v for k, v in params.items() if k != 'cursor'},
             'complete': not bool(cursor), 'pages': previous_pages + page + 1,
             'next_cursor': cursor, 'items': items})
        print(f'{endpoint}: page {page + 1}, {len(items)} records.', flush=True)
        if not cursor:
            complete = True
            break
        if cursor in seen:
            raise RuntimeError('Repeated pagination cursor; stopped.')
        seen.add(cursor)
        params = {**params, 'cursor': cursor}
    return {'records': len(items), 'complete': complete}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-pages', type=int, default=10)
    parser.add_argument('--delay', type=float, default=1.5)
    parser.add_argument('--languages', nargs='+', default=['pt'])
    parser.add_argument('--country-id', help='Collect public events and battles for this country.')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.max_pages < 1 or args.delay < 0:
        parser.error('max-pages must be positive and delay nonnegative')
    output = args.output or ROOT / 'data' / 'warera' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    client = Client(key_from_env(), output, args.delay)
    manifest = {'started_at_utc': datetime.now(timezone.utc).isoformat(), 'collections': {}}
    save(output / 'manifest.json', manifest)
    if not (output / 'countries.json').exists():
        countries = client.get('country.getAllCountries', {})
        save(output / 'countries.json', countries)
    manifest['collections']['articles'] = paginate(client, 'article.getArticlesPaginated',
        {'type': 'last', 'limit': 100, 'languages': args.languages}, args.max_pages)
    if args.country_id:
        for endpoint in ('event.getEventsPaginated', 'battle.getBattles'):
            manifest['collections'][endpoint] = paginate(client, endpoint,
                {'limit': 100, 'countryId': args.country_id}, args.max_pages)
    manifest['finished_at_utc'] = datetime.now(timezone.utc).isoformat()
    save(output / 'manifest.json', manifest)
    print(f'Saved to {output}', flush=True)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, OSError, ValueError) as exc:
        print(f'Collection stopped: {exc}', file=sys.stderr)
        sys.exit(1)
