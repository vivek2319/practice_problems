"""
Ql. Maximum Possible Number by Binary Concatenation 
4 pt. You are given an array of integers nuns of size 3. Return the maximum possible number whose binary representation can be formed by concatenating the binary representation of all elements in nuns in some order. 
Note that the binary representation of any number does not contain leading zeros. 
Example 1: Input: nums = [1,2,3] Output: 30 Explanation: Concatenate the numbers in the order [3, 1, 2] to get the result "11110", which is the binary 



Example 2: Input nums = [2,8,16] Output: 1296 Explanation: 
Concatenate the numbers in the order [2, 8, 16] to get the result "10100010000" , which is the binary representation of 1296. 
Constraints: • 11UMS. Length == 3 • 1 c= nums [1] c= 127
"""

from itertools import permutations
from typing import List

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        # Generate all permutations of the 3 numbers
        all_permutations = permutations(nums)
        
        max_value = 0
        
        # Iterate through each permutation
        for perm in all_permutations:
            # Convert each number to binary (without '0b' prefix)
            binary_string = ''.join(bin(num)[2:] for num in perm)
            
            # Convert the binary string back to an integer
            decimal_value = int(binary_string, 2)
            
            # Update the maximum value if the current one is greater
            max_value = max(max_value, decimal_value)
        
        return max_value
