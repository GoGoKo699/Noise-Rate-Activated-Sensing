"""Structural checks for the common learning map and canonical reader routes.

These assertions do not certify pedagogy, understanding, or scientific truth.
"""
from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from check_rendering import hosted_paths

MAP = ROOT / 'learning/MILESTONES.md'
FIELDS = ('Central question', 'Understanding target', 'Prerequisites',
          'Story role', 'Conceptual connection', 'Canonical sources')
SCIENCE = ('model', 'precision_bounds', 'preset_protocols', 'stopped_sensing',
           'global_precision', 'physical_scope', 'residual_dephasing', 'interpretation')


def records():
    text = MAP.read_text(encoding='utf-8')
    matches = list(re.finditer(r'^### M(\d{2}) ([^\n]+)$', text, re.M))
    return [(int(m[1]), text[m.end():matches[i + 1].start() if i + 1 < len(matches) else len(text)])
            for i, m in enumerate(matches)]


class SharedStructureTests(unittest.TestCase):
    def test_exact_milestone_count_and_allocation(self):
        self.assertEqual([i for i, _ in records()], list(range(1, 31)))
        text = MAP.read_text(encoding='utf-8')
        first, second = text.split('## Phase II: narrative and innovation')
        self.assertEqual(len(re.findall(r'^### M\d{2} ', first, re.M)), 13)
        self.assertEqual(len(re.findall(r'^### M\d{2} ', second, re.M)), 17)

    def test_every_target_has_the_required_fields_and_sources(self):
        for number, body in records():
            with self.subTest(milestone=number):
                for field in FIELDS:
                    value = re.findall(r'\*\*' + re.escape(field) + r'\.\*\* ([^\n]+)', body)
                    self.assertEqual(len(value), 1, field)
                    self.assertTrue(value[0].strip())
                sources = body.split('**Canonical sources.**', 1)[1].split('\n')[0]
                self.assertIn('](', sources)

    def test_dependencies_are_earlier_and_both_phases_integrate(self):
        ancestors = {}
        for number, body in records():
            line = body.split('**Prerequisites.**', 1)[1].split('\n')[0]
            deps = set(map(int, re.findall(r'\[M(\d{2})\]', line)))
            self.assertTrue(all(0 < d < number for d in deps), number)
            ancestors[number] = deps | set().union(*(ancestors[d] for d in deps))
        self.assertEqual(ancestors[13], set(range(1, 13)))
        self.assertEqual(ancestors[30], set(range(1, 30)))

    def test_anchor_and_milestone_entrypoints(self):
        for name in ('README.md', 'llms.txt', 'learning/README.md',
                     'learning/HAASE_BRIDGE.md', 'learning/TUTORIAL.md'):
            text = (ROOT / name).read_text(encoding='utf-8')
            self.assertIn('MILESTONES.md', text, name)
            self.assertIn('1807.11882v4', text, name)

    def test_topic_homes_without_superseded_duplicates(self):
        for name in SCIENCE:
            self.assertTrue((ROOT / f'science/{name}.md').is_file(), name)
        for name in ('docs', 'literature', 'manuscript'):
            self.assertFalse((ROOT / name).exists(), name)
        self.assertFalse((ROOT / 'science/main.md').exists())
        self.assertTrue((ROOT / 'references/references.bib').is_file())
        self.assertTrue((ROOT / 'verification/README.md').is_file())

    def test_shared_material_has_no_personal_assessment_procedure(self):
        forbidden = ('Revise → Learn → Test', '## Coaching and readiness',
                     'next challenge', 'retry rules', 'click-to-select answer',
                     'six domains', 'gogoko699/guinevere')
        paths = [ROOT / 'README.md', ROOT / 'llms.txt', ROOT / 'AGENTS.md']
        paths += list((ROOT / 'learning').glob('*.md'))
        for path in paths:
            text = path.read_text(encoding='utf-8').lower()
            for phrase in forbidden:
                self.assertNotIn(phrase.lower(), text, (path.name, phrase))

    def test_hosted_selection_covers_every_shared_markdown_page(self):
        expected = {'README.md'}
        for section in ('science', 'learning', 'references', 'verification'):
            expected.update(p.relative_to(ROOT).as_posix() for p in (ROOT / section).rglob('*.md'))
        actual = hosted_paths()
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(set(actual), expected)
        self.assertIn('learning/MILESTONES.md', actual)
        self.assertIn('science/precision_bounds.md', actual)

    def test_hosted_selection_fails_when_a_section_is_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                hosted_paths(Path(directory))


if __name__ == '__main__':
    unittest.main()
