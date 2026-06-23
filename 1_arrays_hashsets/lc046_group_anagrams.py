"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

import unittest
from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  sort the array
        # add into a defaultdict
        # output the values

        anagram_map = defaultdict(list)

        for i in strs:
            sorted_str = "".join(sorted(i))
            anagram_map[sorted_str].append(i)

        return list(anagram_map.values())


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

        actual = self.sol.groupAnagrams(input_strs)

        # Sort internal lists and then the outer list for reliable comparison
        actual_sorted = sorted([sorted(group) for group in actual])
        expected_sorted = sorted([sorted(group) for group in expected])

        self.assertEqual(actual_sorted, expected_sorted)

    def test_2(self):
        self.assertEqual(self.sol.groupAnagrams([""]), [[""]])

    def test_3(self):
        self.assertEqual(self.sol.groupAnagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()
