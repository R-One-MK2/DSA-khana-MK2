# Leetcode 217 Contains Duplicate 20260618
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


# Leetcode 242 Valid Anagram 20260620
#### The Problem
```
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
```
#### Solution
- 
##### Pseudocode
###### Brute Force
```python 
# BRUTE FORCE
# create a dictionary of alphabets
# take two for loops, one inner and one outer
# register the letter (only letters, else reject), add dictionary and count it
# as a follow up, do the same thing for the target, if fail, exit
```

Time : 
$$O(N^2)$$
Space :
$$O(1)$$
###### Optimized Short Circuit 
```python 

class Solution:
    # BRUTE FORCE
    # create a dictionary of alphabets
    # take two for loops, one inner and one outer
    # register the letter (only letters, else reject), add dictionary and count it
    # as a follow up, do the same thing for the target, if fail, exit

    # OPTIMAL 1 TWO HASHMAP
    # create hashmap for source
    # create hashmap for target
    # compare

    # error out on length difference



    # OPTIMAL 2 SINGLE HASHMAP
    # create hashmap for source
    # Do increment decrement  on the same hashmap for target

    # False on length mismatch

    # OPTIMAL 3
    # use python counter function
    # Compare the counters of source and target

```

Time : 
$$O(N)$$
Space : 
$$O(1)$$
##### Solution 
```python 

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

```
#### The Pattern
- **Frequency Counter / Hash Mapping**: Using a hashable structure to collect and compare element distributions.
- **Early Exit / Short-Circuiting**: Filtering out bad data instantly (via length checks or missing keys) to prevent redundant computing. 
#### The Architect's Why
- **Decoupling Loops**: Converting nested loops (O(N²)) into sequential loops (O(N)) dramatically speeds up throughput for large data payloads.
- **In-Memory Bounding**: Restricting the tracking state to the unique character set (K=26) protects systems against memory exhaustion vulnerabilities.
#### Real World System Mapping
- [[Order-Independent Verification]]: Validating that an incoming stream of data packets or warehouse inventory items exactly matches a target invoice, regardless of the sequence in which they arrive.
#### Time Complexity
>`How many operations does this perform as the input grows?`
- [[Big O Linear|Linear Complexity]]
#### Space Complexity
>`How much additional memory does this algorithm require to complete its task?`
- [[Big O Constant|Constant Complexity]]

#### Related Patterns 
1. 
#### Related
1. [[anagram]]
#### References
1. [2287. Rearrange Characters to Make Target String - In-Depth Explanation](https://algo.monster/liteproblems/2287)

# Leetcode 001 Two Sum 20260622

| Concept | Note |
| ------- | ---- |
|         |      |

#### The Problem
```
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
```
#### Solution
```python

```
##### Pseudocode
###### Brute Force
```python 

```

Time : 
Space : 
###### Optimised Short Circuit 
```python 
# Iterate through an array
# Create a dictionary called seen
# Make a compliment and see if it is in seen, else add in dictionary
# Continue 
```

Time : [[Big O Linear|Linear Complexity]]
Space : [[Big O Linear|Linear Complexity]]
##### Solution 
```python 

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
```
#### The Pattern
- [[Hashing]] /[[Hash Map]] / [[Associative Array]]
#### The Architect's Why
- We use the Hash Map as "memory." By storing `value: index` as we traverse the array, we can check for the required complement in $O(1)$ time, transforming an expensive exhaustive search into a single linear pass
#### Real World System Mapping
- 
#### Time Complexity
>`How many operations does this perform as the input grows?`

We perform a single pass through the array. For each element, dictionary lookups and insertions are $O(1)$ on average. Total operations scale linearly with input $n$.
#### Space Complexity
>`How much additional memory does this algorithm require to complete its task?`

In the worst case (the solution is the last pair, or doesn't exist), we store $n$ elements in the hash map.
#### The Gap Bounty

#### Related Patterns 
1. [[Two Pointers]]
2. [[Hash Set]]
#### Related
1. [[Hash Set]]
2. [[Hash Map]]
3. [[Two Pointers]]
#### References
1. Introduction to Algorithms (CLRS): Chapter on Hash Tables.
2. Grokking Algorithms: Chapter on Hash Tables.
