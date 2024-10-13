"""
You are given a string source of size n, a string pattern that is a subsequence of source. anda
sorted integer array targetIndices that contains distinct numbers in the range [0, n - 1].
We define an operation as removing a character at an index idx from source such that:

© idx is an element of targetIndices,

© pattern remains a subsequence of source after removing the character.

Performing an operation does not change the indices of the other characters in source. For
example, if you remove 'c' from "acb", the character at index 2 would still be 'b'.

Return the maximum number of operations that can be performed,

A subsequence is a string that can be derived from another string by deleting some or no
characters without changing the order of the remaining characters.


Example 1:
Input: source = "abbaa", pattern = "aba", targetindices = [0,1,2]
Output: 1
Explanation:
We can't remove any character from source but we can do either of these two operations: 
¢ Remove source[1],so that source becomes "a_baa”.
© Remove source[2],so that source becomes "ab_aa”.
Example 2:
Input: source = "bcda", pattern = "d", targetindices = [0,3]
Output: 2

Example 3:

Example 3:
Input: source = "dda", pattern = "dda", targetlndices = [0,1,2]
Output: @
Explanation:
We can't remove any character from source.
Example 4:
Input: source = "yeyeykyded", pattern = "yeyyd", targetindices = [0,2,3,4]
Output: 2
Explanation:
We can remove source[2] and source[3] in two operations.

    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:

"""

from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        
        # Function to calculate the x-sum for a subarray
        def calculate_x_sum(subarray: List[int], x: int) -> int:
            count = Counter(subarray)  # Count the frequency of elements in the subarray
            # Sort by frequency first (descending), and then by value (descending)
            sorted_elements = sorted(count.items(), key=lambda y: (-y[1], -y[0]))
            x_sum = 0
            elements_used = 0
            for value, freq in sorted_elements:
                if elements_used >= x:
                    break
                # Add all occurrences of this element to the sum
                x_sum += value * freq
                elements_used += 1
            return x_sum
        
        # Sliding window over the array for subarrays of length k
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            # Append the x-sum for the current subarray to the result list
            result.append(calculate_x_sum(subarray, x))
        
        return result
