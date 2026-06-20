"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"

Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

import unittest
from collections import Counter


class Solution:
    # BRUTE FORCE
    # create a dictionary of alphabets
    # take two for loops, one inner and one outer
    # register the letter (only letters, else reject), add dictionary and count it
    # as a follow up, do the same thing for the target, if fail, exit

    def isAnagram_optimal_1(self, s: str, t: str) -> bool:
        # OPTIMAL 1 TWO HASHMAP
        # create hashmap for source
        # create hashmap for target
        # compare

        # error out on length difference
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        return s_map == t_map

    def isAnagram_optimal_2(self, s: str, t: str) -> bool:
        # OPTIMAL 2 SINGLE HASHMAP
        # create hashmap for source
        # Do increment decrement  on the same hashmap for target

        # False on length mismatch
        if len(s) != len(t):
            return False

        # Create hashmap for the source
        map_count = {}

        # Add source string if found
        for char in s:
            map_count[char] = map_count.get(char, 0) + 1

        # Remove count if found
        for char in t:
            # If not found, NOT anagram
            if char not in map_count or map_count[char] == 0:
                return False

            # If found, reduce the COUNT
            map_count[char] -= 1

        return True

    def isAnagram_optimal_3(self, s: str, t: str) -> bool:
        # OPTIMAL 3
        # use python counter function
        # Compare the counters of source and target
        return Counter(s) == Counter(t)


class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_string(self):
        self.assertTrue(self.sol.isAnagram_optimal_1("a", "a"))
        self.assertTrue(self.sol.isAnagram_optimal_2("a", "a"))
        self.assertTrue(self.sol.isAnagram_optimal_3("a", "a"))

    def test_valid_anagram(self):
        self.assertTrue(self.sol.isAnagram_optimal_1("anagram", "nagaram"))
        self.assertTrue(self.sol.isAnagram_optimal_2("anagram", "nagaram"))
        self.assertTrue(self.sol.isAnagram_optimal_3("anagram", "nagaram"))

    def test_invalid_anagram(self):
        self.assertFalse(self.sol.isAnagram_optimal_1("cat", "rat"))
        self.assertFalse(self.sol.isAnagram_optimal_2("cat", "rat"))
        self.assertFalse(self.sol.isAnagram_optimal_3("cat", "rat"))


if __name__ == "__main__":
    unittest.main()
