"""Inspect public GitHub-hosted Markdown at an immutable commit.

Requires the optional Playwright and Pillow packages and a Chromium install.
No authentication, repository writes, or third-party rendering service is used.
The generated screenshots require visual review in addition to this DOM check.
"""
from __future__ import annotations

import argparse
import base64
import io
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'GoGoKo699/Noise-Rate-Activated-Sensing'
PAGES = ('README.md', 'docs/TUTORIAL.md', 'docs/THEOREMS.md',
         'docs/LEARNING_GUIDE.md', 'docs/PRESET_PROTOCOLS.md',
         'docs/STOPPED_SENSING.md', 'docs/GLOBAL_RISK.md',
         'docs/SCIENTIFIC_SYNTHESIS.md', 'docs/PHYSICAL_SCOPE.md',
         'docs/RESIDUAL_DEPHASING.md')


def math_count(text: str) -> int:
    """Count the repository's dollar-delimited formulas outside code fences."""
    text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)
    return len(re.findall(r'(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$[^\n$]+?(?<!\\)\$',
                          text, flags=re.S))


# GitHub's math custom elements use shadow roots. Inspect the actual generated
# DOM rather than accepting raw LaTeX inside an uninitialized element.
INSPECT = r'''root => {
  function nodes(r) {
    const out = [...r.querySelectorAll('*')];
    for (const e of [...out]) if (e.shadowRoot) out.push(...nodes(e.shadowRoot));
    return out;
  }
  const all = nodes(root);
  const renderers = all.filter(e => e.localName === 'math-renderer');
  const done = e => nodes(e).some(n => n.localName === 'mjx-container' ||
      n.classList.contains('katex') || n.localName === 'math' || n.localName === 'svg');
  const errors = all.filter(e => e.matches('merror, mjx-merror, .katex-error, .MathJax_Error, [data-mjx-error]'))
      .map(e => (e.textContent || e.getAttribute('data-mjx-error') || '').slice(0, 240));
  return {math_elements: renderers.length,
          rendered: renderers.filter(done).length,
          errors: errors,
          heading: root.querySelector('h1')?.innerText || '',
          links: [...root.querySelectorAll('a[href]')].length,
          article_width: root.getBoundingClientRect().width,
          overflow: root.scrollWidth > root.clientWidth + 3,
          sample_html: renderers.length ? renderers[0].outerHTML.slice(0, 1500) : root.innerHTML.slice(0, 1500)};
}'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref', required=True, help='Full commit SHA, never a moving branch')
    parser.add_argument('--output', type=Path, required=True, help='Artifact directory outside tracked sources')
    parser.add_argument('--log-previews', action='store_true', help='Also emit compact public screenshot previews as base64')
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.ref):
        parser.error('--ref must be a full lowercase commit SHA')
    from playwright.sync_api import sync_playwright
    from PIL import Image

    args.output.mkdir(parents=True, exist_ok=True)
    report = {'repository': REPOSITORY, 'commit': args.ref, 'pages': [],
              'scope': 'Hosted DOM and screenshots; visual review and scientific review are separate.'}
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context(viewport={'width': 1280, 'height': 900},
                                      device_scale_factor=1, color_scheme='light')
        for path in PAGES:
            page = context.new_page()
            url = f'https://github.com/{REPOSITORY}/blob/{args.ref}/{quote(path)}'
            item = {'path': path, 'url': url, 'status': 'failed'}
            try:
                source = subprocess.run(['git', 'show', f'{args.ref}:{path}'], cwd=ROOT,
                                        check=True, capture_output=True, text=True).stdout
                item['expected_math'] = math_count(source)
                response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                if response is None or response.status != 200:
                    raise RuntimeError(f'HTTP {None if response is None else response.status}')
                article = page.locator('.markdown-body').first
                article.wait_for(state='visible', timeout=60000)
                # Activate lazy formula rendering throughout the article.
                height = page.evaluate('document.documentElement.scrollHeight')
                for y in range(0, height, 650):
                    page.evaluate('(y) => window.scrollTo(0, y)', y)
                    page.wait_for_timeout(70)
                page.evaluate('window.scrollTo(0, 0)')
                for _ in range(40):
                    data = article.evaluate(INSPECT)
                    if data['rendered'] == item['expected_math'] or data['errors']:
                        break
                    page.wait_for_timeout(250)
                item.update(data)
                name = path.replace('/', '__').replace('.md', '')
                page.screenshot(path=str(args.output / f'{name}.png'), full_page=True)
                if path in PAGES[:3]:
                    displays = article.locator('math-renderer.js-display-math')
                    target = displays.nth(min(2, displays.count()-1)) if displays.count() else article.locator('h1')
                    target.scroll_into_view_if_needed()
                    box = target.bounding_box()
                    if box:
                        page.evaluate('(y) => window.scrollBy(0, y)', box['y']-200)
                    raw = page.screenshot()
                    image = Image.open(io.BytesIO(raw))
                    article_box = article.bounding_box()
                    left = max(0, int(article_box['x'])) if article_box else 0
                    width = min(1000, int(article_box['width'])) if article_box else 1000
                    image = image.crop((left, 90, min(1280, left+width), 740))
                    image.thumbnail((850, 580))
                    preview = io.BytesIO()
                    image.save(preview, format='WEBP', quality=55, method=6)
                    (args.output / f'{name}.webp').write_bytes(preview.getvalue())
                    if args.log_previews:
                        print(f'NRAS_PREVIEW {name} {base64.b64encode(preview.getvalue()).decode()}', flush=True)
                if data['math_elements'] != item['expected_math']:
                    raise RuntimeError('Hosted formula count differs from source; inspect the screenshot and HTML sample')
                if data['rendered'] != data['math_elements'] or data['errors']:
                    raise RuntimeError('Unrendered or invalid mathematics in the hosted page')
                if not data['heading']:
                    raise RuntimeError('Missing document heading')
                item['status'] = 'passed'
            except Exception as exc:
                item['error'] = f'{type(exc).__name__}: {exc}'
            finally:
                page.close()
                report['pages'].append(item)
                print(json.dumps(item), flush=True)
        browser.close()
    (args.output / 'report.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    return 0 if all(p['status'] == 'passed' for p in report['pages']) else 1


if __name__ == '__main__':
    sys.exit(main())
