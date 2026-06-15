"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_array(self):
        self.assertFalse(self.sol.containsDuplicate([]))

    def test_simple_element(self):
        self.assertFalse(self.sol.containsDuplicate([1]))

    def test_no_duplicate(self):
        self.assertFalse(self.sol.containsDuplicate([1, 2, 3, 4]))

    def test_single_duplicate(self):
        self.assertTrue(self.sol.containsDuplicate([1, 2, 3, 1]))

    def test_multiple_duplicates(self):
        self.assertTrue(self.sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main()
