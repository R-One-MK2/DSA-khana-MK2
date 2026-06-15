# Leetcode 217 Contains Duplicate
> [!summary] Summary
> Summary of the File 
> 

| Concept         | Note |
| --------------- | ---- |
| [[Hash Set]]    |      |
| [[O(n) Linear]] |      |
#### The Problem
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

```
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
```
#### Solution
- make a set, and make it into an array(list)
- compare the set with the original array
##### Pseudocode
###### Brute Force
```python 
function contains_duplicate(nums): 
	create a set called nums_hashmap
	return compare the length of the set and list 
```

Time : [[O(n) Linear]]
Space : [[O(n) Linear]]
###### Optimised Short Circuit 
```python 
function contains_duplicate(nums):
	a empty set named seen
	for each num in nums: 
	   if num in seen: 
		   return true 
		add num to seen 
	return false
```

##### Solution 
```python 
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

```
#### The Pattern
[[Hash Set]]
#### The Architect's Why
- It gives [[O(1) Constant]] average time complexity for insertions 
#### Real World System Mapping
1. Check if the username exists : In a social media application we can check if the username already exists for registration. 
2. Counting the frequency of Occurrences 
#### Time Complexity
>`How many operations does this perform as the input grows?`
- Since we iterate through the list once to populate the set, the time complexity is [[O(n) Linear]] time
#### Space Complexity
>`How much additional memory does this algorithm require to complete its task?`
- Since the `set` stores unique elements from the original array, in the worst case where all elements are distinct, the set will contain $n$ elements. Because the memory usage scales directly in proportion to the number of elements in the input, we define this as [[O(n) Linear]] space

#### The Gap Bounty
1. Edge Case  when the empty or 1 element 
#### Related Patterns 
1. [[Sliding Window]]
2. [[Two Pointers]]
#### Related
1. [[Hash Set]]
2. [[Hashing]]
3. [[Big O Notation]]
4. [[O(1) Constant]]
5. [[O(n) Linear]]
6. [[O(n2) Quadratic]]

#### References
1. 
