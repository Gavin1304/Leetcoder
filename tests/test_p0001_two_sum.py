import unittest

from solutions.p0001_two_sum import Solution


class TwoSumTests(unittest.TestCase):
    def test_finds_pair(self):
        self.assertCountEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_handles_duplicate_values(self):
        self.assertCountEqual(Solution().twoSum([3, 3], 6), [0, 1])

    def test_handles_negative_values(self):
        self.assertCountEqual(Solution().twoSum([-3, 4, 3, 90], 0), [0, 2])
