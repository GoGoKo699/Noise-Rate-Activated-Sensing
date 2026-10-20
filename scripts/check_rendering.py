"""Check actual public GitHub mathematics at an immutable commit.

Playwright and Chromium are optional dependencies, imported only for the
networked browser audit. Source parsing can be tested offline. Screenshots and
the exact audited sources remain CI artifacts, not tracked generated content.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'GoGoKo699/Noise-Rate-Activated-Sensing'
FENCE = re.compile(r'^```([^\n]*)\n(.*?)^```[ \t]*(?:\n|$)', re.M | re.S)
INLINE = re.compile(r'(?<!\\)\$`(?P<protected>[^`\n]+)`\$|(?P<code>`[^`\n]*`)|(?<!\\)\$\$(?P<display>.*?)\$\$|(?<!\\)\$(?P<legacy>[^$\n]+)\$', re.S)
MATRIX = re.compile(r'\\begin\{(pmatrix|bmatrix|matrix|Bmatrix|vmatrix|Vmatrix)\}(.*?)\\end\{\1\}', re.S)


def math_fragments(text: str) -> list[str]:
    """Extract protected or legacy math; exclude ordinary fenced/code spans.

    Legacy formulas remain detectable so the source check can diagnose them
    rather than silently accepting a lower expected count in the browser.
    """
    parts: list[tuple[int, str]] = []
    outside = list(text)
    for match in FENCE.finditer(text):
        if match[1].strip() == 'math':
            parts.append((match.start(), match[2].strip()))
        outside[match.start():match.end()] = ' ' * (match.end() - match.start())
    residue = ''.join(outside)
    for match in INLINE.finditer(residue):
        if match['code'] is None:
            parts.append((match.start(), next(group for group in match.groups() if group is not None).strip()))
    return [body for _, body in sorted(parts)]


def math_count(text: str) -> int:
    return len(math_fragments(text))


def matrix_rows(formulas: list[str]) -> list[int]:
    """Expected row counts for the repository's non-nested matrix environments."""
    rows = []
    for formula in formulas:
        for matrix in MATRIX.finditer(formula):
            body = matrix[2].strip()
            if body.endswith('\\\\'):
                body = body[:-2]
            rows.append(len(re.findall(r'\\\\', body)) + 1)
    return sorted(rows)


def source_math_issues(text: str) -> list[str]:
    """Reject the serialization patterns found to corrupt this repository on GitHub."""
    issues = []
    outside = FENCE.sub(lambda m: ' ' * len(m[0]), text)
    for match in INLINE.finditer(outside):
        if match['legacy'] is not None or match['display'] is not None:
            issues.append('Use protected inline math or a math fence, not bare dollar delimiters')
    for formula in math_fragments(text):
        if r'\operatorname' in formula:
            issues.append('Use the checked upright named-function notation instead of operatorname')
    if sum(line.startswith('```') for line in text.splitlines()) % 2:
        issues.append('Unbalanced code or math fences')
    return issues


INSPECT = r'''root => {
  function nodes(r) {
    const out = [...r.querySelectorAll('*')];
    for (const e of [...out]) if (e.shadowRoot) out.push(...nodes(e.shadowRoot));
    return out;
  }
  const all = nodes(root);
  const renderers = all.filter(e => e.localName === 'math-renderer');
  const done = e => nodes(e).some(n => n.localName === 'mjx-container' ||
      n.classList.contains('katex') || n.localName === 'math');
  const errors = all.filter(e => e.matches('merror, mjx-merror, .katex-error, .MathJax_Error, [data-mjx-error]'))
      .map(e => (e.textContent || e.getAttribute('data-mjx-error') || '').slice(0, 240));
  const unrendered = renderers.filter(e => !done(e)).map(e =>
      ((e.innerText || '') + ' ' + (e.shadowRoot?.textContent || '')).trim().slice(0, 600));
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const raw = [];
  while (walker.nextNode()) {
    const n = walker.currentNode;
    if (n.textContent.includes('$') && !n.parentElement.closest('math-renderer,pre,code'))
      raw.push(n.textContent.trim().slice(0, 400));
  }
  const rows = all.filter(e => e.localName === 'mtable').map(e =>
      [...e.children].filter(n => ['mtr','mlabeledtr'].includes(n.localName)).length).sort((a,b)=>a-b);
  return {math_elements: renderers.length, rendered: renderers.filter(done).length,
          errors, unrendered, raw_dollar_text: raw, matrix_rows: rows,
          heading: root.querySelector('h1')?.innerText || '',
          links: root.querySelectorAll('a[href]').length,
          article_width: root.getBoundingClientRect().width,
          overflow: root.scrollWidth > root.clientWidth + 3};
}'''



def hosted_paths(root: Path = ROOT) -> list[str]:
    """All shared reader pages; missing sections are failures, not skipped audits."""
    paths = ['README.md']
    for directory in ('science', 'learning', 'references', 'verification'):
        folder = root / directory
        if not folder.is_dir():
            raise FileNotFoundError(f'Missing reader section: {directory}')
        paths.extend(p.relative_to(root).as_posix() for p in sorted(folder.rglob('*.md')))
    if not (root / 'README.md').is_file():
        raise FileNotFoundError('Missing reader entrypoint: README.md')
    return paths



def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref', required=True, help='Full commit SHA, never a moving branch')
    parser.add_argument('--output', type=Path, required=True, help='Untracked artifact directory')
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.ref):
        parser.error('--ref must be a full lowercase commit SHA')
    from playwright.sync_api import sync_playwright

    paths = hosted_paths()
    args.output.mkdir(parents=True, exist_ok=True)
    report = {'repository': REPOSITORY, 'commit': args.ref, 'pages': [],
              'scope': 'Actual hosted DOM and screenshots; visual and scientific review are separate.'}
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context(viewport={'width': 1280, 'height': 900},
                                      device_scale_factor=1, color_scheme='light')
        for path in paths:
            page = context.new_page()
            url = f'https://github.com/{REPOSITORY}/blob/{args.ref}/{quote(path)}'
            item = {'path': path, 'url': url, 'status': 'failed'}
            name = path.replace('/', '__').removesuffix('.md')
            try:
                source = subprocess.run(['git', 'show', f'{args.ref}:{path}'], cwd=ROOT,
                                        check=True, capture_output=True, text=True).stdout
                formulas = math_fragments(source)
                item['expected_math'] = len(formulas)
                item['expected_matrix_rows'] = matrix_rows(formulas)
                response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                if response is None or response.status != 200:
                    raise RuntimeError(f'HTTP {None if response is None else response.status}')
                article = page.locator('.markdown-body').first
                article.wait_for(state='visible', timeout=60000)
                height = page.evaluate('document.documentElement.scrollHeight')
                for y in range(0, height, 650):
                    page.evaluate('(y) => window.scrollTo(0, y)', y)
                    page.wait_for_timeout(70)
                page.evaluate('window.scrollTo(0, 0)')
                for _ in range(40):
                    data = article.evaluate(INSPECT)
                    if data['rendered'] == len(formulas) or data['errors']:
                        break
                    page.wait_for_timeout(250)
                item.update(data)
                page.screenshot(path=str(args.output/f'{name}.png'), full_page=True)
                (args.output/f'{name}.html').write_text(article.inner_html(), encoding='utf-8')
                if data['math_elements'] != len(formulas):
                    raise RuntimeError('Hosted formula count differs from source')
                if data['rendered'] != data['math_elements'] or data['errors']:
                    raise RuntimeError('Unrendered or invalid hosted mathematics')
                if data['raw_dollar_text']:
                    raise RuntimeError('Raw math delimiters remain outside rendered formulas')
                if data['matrix_rows'] != item['expected_matrix_rows']:
                    raise RuntimeError('Hosted matrix rows differ from source')
                if data['overflow']:
                    raise RuntimeError('Article overflows its available width; inspect screenshot')
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
    (args.output/'report.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    return 0 if all(p['status'] == 'passed' for p in report['pages']) else 1


if __name__ == '__main__':
    sys.exit(main())
