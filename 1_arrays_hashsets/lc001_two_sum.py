"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        # Iterate over the row
        for i, item in enumerate(nums):
            complement = target - item

            if complement in seen:
                return [seen[complement], i]

            seen[item] = i
        # complement = target - element
        # check if complement == next item else add to seen

        # Time Complexity : O(N)
        # Space Complexity : O(N)


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_2(self):
        self.assertEqual(self.sol.twoSum([3, 2, 4], 6), [1, 2])

    def test_3(self):
        self.assertEqual(self.sol.twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
