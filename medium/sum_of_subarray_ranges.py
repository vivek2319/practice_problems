"""
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109

"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def calculate_subarray_sums(nums):            
            stack = []
            n = len(nums)
            left_indices = [-1] * n
            right_indices = [n] * n

            # Calculate the left indices
            for i, value in enumerate(nums):
                while stack and nums[stack[-1]] <= value:
                    stack.pop()
                if stack:
                    left_indices[i] = stack[-1]
                stack.append(i)
            
            # Reset the stack for right indices calculation
            stack = []

            # Calculate the right indices
            for i in range(n-1, -1, -1):
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                if stack:
                    right_indices[i] = stack[-1]
                stack.append(i)
            
            # Calculate final sum
            return sum((i - left_indices[i]) * (right_indices[i] -i) * value for i, value in enumerate(nums))
        # Calculate maximum values sum
        max_sum = calculate_subarray_sums(nums)

        #calculate minimum values sum (inverting the values)
        min_sum =  calculate_subarray_sums([-value for value in nums])

        # return the total sum
        return max_sum + min_sum
        


        
