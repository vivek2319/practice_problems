"""
The factor score of an array is defined as the product of the LCM and GCD of all elements of that array. 
Return the maximum factor score of nums after removing at most one element from it. 
Note that both the LCM and GCD of a single number are the number itself, and the factor score of an empty array is O. 
The term 1.cm (a, b) denotes the least common multiple of a and b. 
The term gcd (a, b) denotes the greatest common divisor of a and b . 
Example 1: Input: nums = [2,4,8,16] Output: 64 Explanation: On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a 


maximum factor score of 4 * 16 = 64. Example 2: Input: nums = [1,2,3,4,5] Output: 60 Explanation: The maximum factor score of 60 can be obtained without removing any elements. Example 3: Input: nums = [3] Output: 9 
Constraints: • 1 <= nuns. length <= 100 • 1 <= nuns(i) <= 30 


def maxScore(self, nums: List[int]) -> int:
"""

from typing import List
from math import gcd
from functools import reduce

class Solution:
        @staticmethod
        def lcm(a, b):
            return (a * b) // gcd(a, b)
            
        @staticmethod
        def lcm_of_array(arr):
            return reduce(lcm, arr)
        
        @staticmethod
        def gcd_of_array(arr):
            return reduce(gcd, arr)
    
        
        def maxScore(self, nums: List[int]) -> int:
            n = len(nums)
            if n == 1:
                # Edge case: Only one element, return its square
                return nums[0] * nums[0]
    
            # Calculate the GCD and LCM of the entire array without removal
            total_gcd = Solution.gcd_of_array(nums)
            total_lcm = Solution.lcm_of_array(nums)
            max_factor_score = total_gcd * total_lcm
    
            # Try removing each element and calculate the factor score
            for i in range(n):
                # Remaining array without the i-th element
                remaining = nums[:i] + nums[i+1:]
                current_gcd = Solution.gcd_of_array(remaining)
                current_lcm = Solution.lcm_of_array(remaining)
                max_factor_score = max(max_factor_score, current_gcd * current_lcm)
    
            return max_factor_score
