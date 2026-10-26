"""Compile the self-contained report in a new directory using TeX Live 2025."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'learning/source/Noise_Rate_Activated_Sensing_Report.tex'


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='New build directory; must not already exist')
    parser.add_argument('--pdflatex', default='pdflatex',
                        help='TeX Live 2025 pdfLaTeX executable')
    args = parser.parse_args()
    engine = shutil.which(args.pdflatex)
    if not engine:
        parser.error('pdfLaTeX executable not found')
    # Keep the pdflatex entry point: resolving its symlink would select pdftex.
    engine = str(Path(engine).absolute())
    version = subprocess.run([engine, '--version'], check=True, text=True,
                             capture_output=True).stdout.splitlines()[0]
    if 'pdfTeX' not in version or 'TeX Live 2025' not in version:
        parser.error(f'TeX Live 2025 pdfLaTeX required; found {version}')
    output = args.output.resolve()
    if output.exists():
        parser.error(f'output directory already exists: {output}')
    output.mkdir(parents=True)
    source = output / SOURCE.name
    shutil.copyfile(SOURCE, source)
    for pass_number in (1, 2):
        transcript = output / f'console-{pass_number}.txt'
        with transcript.open('w', encoding='utf-8') as stream:
            result = subprocess.run(
                [engine, '-interaction=nonstopmode',
                 '-halt-on-error', '-file-line-error', source.name],
                cwd=output, stdout=stream, stderr=subprocess.STDOUT)
        if result.returncode:
            raise SystemExit(f'Compilation failed; inspect {transcript}')
    pdf = source.with_suffix('.pdf')
    log = source.with_suffix('.log')
    if not pdf.is_file() or not log.is_file() or pdf.stat().st_size == 0:
        raise SystemExit('Fresh PDF and matching final log are required')
    text = log.read_text(encoding='utf-8', errors='replace')
    issues = re.findall(
        r'^.*(?:Warning:|Overfull|Underfull|Missing character:|'
        r'undefined references|Rerun to get).*$', text, flags=re.M)
    if issues:
        raise SystemExit('Final log requires review:\n' + '\n'.join(issues))
    manifest = {
        'engine': version,
        'source': str(SOURCE.relative_to(ROOT)),
        'source_sha256': sha256(source),
        'pdf_sha256': sha256(pdf),
        'log_sha256': sha256(log),
    }
    (output / 'build.json').write_text(
        json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(f'Fresh report and final log: {output}')
    print(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    main()
