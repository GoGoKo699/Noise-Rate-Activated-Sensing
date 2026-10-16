"""Offline regression checks for math serialization and example comparison."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from check_rendering import math_fragments, matrix_rows, source_math_issues
from check_reproducibility import compare


class MathSerializationTests(unittest.TestCase):
    def test_protected_inline_does_not_merge_adjacent_expressions(self):
        text = r'Target $`\omega`$, nuisance $`\phi`$, optimum $`I_\omega^*(T)`$.'
        self.assertEqual(math_fragments(text), [r'\omega', r'\phi', r'I_\omega^*(T)'])
        self.assertFalse(source_math_issues(text))

    def test_math_fences_preserve_backslashes_and_curly_braces(self):
        expression = r'\begin{pmatrix}1&2\\3&4\end{pmatrix},\quad y\in\{+,-\}'
        text = '```math\n' + expression + '\n```\n'
        self.assertEqual(math_fragments(text), [expression])
        self.assertFalse(source_math_issues(text))

    def test_ordinary_code_is_not_counted_as_mathematics(self):
        text = '```bash\necho "$HOME"\n```\n`$not_math$` and $`x`$.'
        self.assertEqual(math_fragments(text), ['x'])
        self.assertFalse(source_math_issues(text))

    def test_formula_order_and_matrix_rows(self):
        text = '$`a`$\n\n```math\n' + r'\begin{pmatrix}a&b\\c&d\end{pmatrix}' + '\n```\n$`z`$'
        formulas = math_fragments(text)
        self.assertEqual((formulas[0], formulas[-1]), ('a', 'z'))
        self.assertEqual(matrix_rows(formulas), [2])
        self.assertEqual(matrix_rows([r'\begin{matrix}a\\b\\\end{matrix}']), [2])

    def test_legacy_delimiters_and_rejected_macro_are_flagged(self):
        for text in ['$x$', '$$\nx^2\n$$', r'$`\operatorname{Poisson}(t)`$', '```math\nx']:
            with self.subTest(text=text):
                self.assertTrue(source_math_issues(text))

    def test_every_document_uses_the_checked_serialization(self):
        paths = list(ROOT.glob('*.md')) + list((ROOT/'docs').glob('*.md'))
        paths += list((ROOT/'literature').glob('*.md'))
        for path in paths:
            with self.subTest(path=path.name):
                self.assertFalse(source_math_issues(path.read_text(encoding='utf-8')))


class RegenerationComparatorTests(unittest.TestCase):
    def test_complete_matching_results(self):
        compare({'rows': [1.0 + 1e-12, True, 'scope']}, {'rows': [1., True, 'scope']})

    def test_changed_structure_or_value_is_not_silently_accepted(self):
        for actual, expected in [({'x':1},{'y':1}), ([1],[1,2]), (True,1),
                                 (float('nan'),1.), (2.,1.), ('a','b')]:
            with self.subTest(actual=actual,expected=expected):
                with self.assertRaises(ValueError):
                    compare(actual,expected)


if __name__ == '__main__':
    unittest.main()
