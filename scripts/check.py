"""Run the scientific suite and offline documentation-structure checks."""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def heading_ids(text):
    ids = set()
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, flags=re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        ids.add(slug)
    return ids


def check_docs():
    checked = 0
    for path in sorted(ROOT.rglob('*.md')) + [ROOT / 'llms.txt']:
        if {'.git', '.venv', 'venv', '__pycache__', '.pytest_cache'} & set(path.parts):
            continue
        text = path.read_text(encoding='utf-8')
        if text.count('$$') % 2:
            raise ValueError(f'unbalanced display math in {path.relative_to(ROOT)}')
        if '\\(' in text or '\\[' in text:
            raise ValueError(f'use dollar-delimited GitHub math in {path.relative_to(ROOT)}')
        for target in re.findall(r'\]\(([^\s)]+)\)', text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not dest.is_relative_to(ROOT) or not dest.exists():
                raise ValueError(f'broken local link {target} in {path.relative_to(ROOT)}')
            if parsed.fragment and dest.suffix == '.md':
                if unquote(parsed.fragment) not in heading_ids(dest.read_text(encoding='utf-8')):
                    raise ValueError(f'broken anchor {target} in {path.relative_to(ROOT)}')
        checked += 1
    print(f'Documentation structure: {checked} files checked. Hosting-renderer appearance is separate.', flush=True)


def main():
    check_docs()
    result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], cwd=ROOT)
    return result.returncode


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(1)
