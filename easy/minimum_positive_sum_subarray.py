"""
You are given an integer array nums and two integers 1. and r. Your task is to find the minimum sum of a subarray whose size is between 1. and r (inclusive) and whose sum is greater than 0. Return the minimum sum of such a subarray. If no such subarray exists, return -1. A subarray is a contiguous non-empty sequence of elements within an array. 
Example 1: Input nums = [3, -2, 1, 4], i = 2, r = 3 Output: 1 Explanation: The subarrays of length between 1. = 2 and r = 3 where the sum is greater than 0 are: • [3, -2] with a sum of 1 • (1, 4] with a sum of 5 • [3, -2, 1] with a sum of 2 • (-2, 1, 4] with a sum of 3 



El Description 'D D Submissions Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1. 
Example 2: 
Input nums = [-2, 2, -3, 1], 1 = 2, r = 3 Output: -1 Explanation: 
There is no subarray of length between 1 and r that has a sum greater than 0. So, the answer is -1. 
Example 3: Input nums = [1, 2, 3, 4], 1 = 2, r = 4 Output: 3 Explanation: The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3. 



"""

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')  
        found = False  

        for start in range(n):
            current_sum = 0
            
            
            for end in range(start, min(start + r, n)):
                current_sum += nums[end]
                
                if end - start + 1 >= l and current_sum > 0:
                    found = True
                    min_sum = min(min_sum, current_sum)
        
        return min_sum if found else -1
