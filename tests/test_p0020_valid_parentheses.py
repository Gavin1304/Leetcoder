import unittest

from solutions.p0020_valid_parentheses import Solution


class ValidParenthesesTests(unittest.TestCase):
    def test_accepts_nested_brackets(self):
        self.assertTrue(Solution().isValid("([]){}"))

    def test_rejects_crossed_brackets(self):
        self.assertFalse(Solution().isValid("([)]"))

    def test_rejects_unmatched_brackets(self):
        for brackets in ("(", "]"):
            with self.subTest(brackets=brackets):
                self.assertFalse(Solution().isValid(brackets))
