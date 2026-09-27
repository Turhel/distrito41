"""Run with local reader running; optional dev dependency: playwright + chromium."""
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from playwright.sync_api import sync_playwright

URL = 'http://127.0.0.1:8041'

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1440, 'height': 1000})
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(URL)
    page.wait_for_function('flip !== null && pages.length > 7')
    def verify_text():
        data = page.evaluate('''() => ({
          expected: chapters.map(chapter => [chapter.title, ...chapter.lines.filter(line=>line.trim())].join(' ')).join(' '),
          actual: pages.slice(1).map(page=>page.content.textContent).join(' '),
          overflow: pages.filter(page=>page.content && page.content.scrollHeight>page.content.clientHeight+2).length
        })''')
        # DOM textContent joins adjacent paragraph nodes without spaces; collect explicitly.
        data['actual'] = page.evaluate("pages.slice(1).flatMap(p=>[...p.content.children].map(el=>el.textContent)).join(' ')")
        normalize = lambda value: re.sub(r'\s+', ' ', value).strip()
        assert normalize(data['expected']) == normalize(data['actual']), 'Text lost or duplicated'
        assert data['overflow'] == 0, data['overflow']
    verify_text()
    page.locator('#next').click()
    page.wait_for_function('flip.getCurrentPageIndex() > 0')
    page.wait_for_timeout(800)
    page.locator('#contents').click()
    page.locator('#chapters button').nth(4).click()
    page.wait_for_function('pages[flip.getCurrentPageIndex()].chapter === 4')
    page.locator('#larger').click()
    verify_text()
    page.reload()
    page.wait_for_function('flip !== null && pages[flip.getCurrentPageIndex()].chapter === 4')
    page.locator('#theme').click()
    assert 'night' in page.locator('body').get_attribute('class')
    page.locator('#mode').click()
    assert page.locator('#continuous').is_visible()
    assert page.locator('#continuous section').count() == 7
    page.locator('#mode').click()
    page.screenshot(path='reader-desktop.png')
    page.set_viewport_size({'width': 390, 'height': 844})
    page.wait_for_timeout(1200)
    verify_text()
    assert page.evaluate('flip.getOrientation()') == 'portrait'
    page.screenshot(path='reader-mobile.png')
    assert not errors, errors
    print('PASS: complete text, no overflow, animation, index, font, saved place, night, flow and mobile.')
    browser.close()

for route in ['/.env', '/../.env', '/%2e%2e/.env', '/scripts/collect_warera.py']:
    try:
        urlopen(URL + route)
        raise AssertionError(f'Unexpected access: {route}')
    except HTTPError as error:
        assert error.code == 404
print('PASS: reader does not serve repository secrets or scripts.')
