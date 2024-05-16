"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""
"""
INTUITION - mark all numbers based on their indices -1

We know that all the numbers are in the range [1, n].
So we mark all the indices of the numbers we saw by making the number negative.
Then, we iterate through the array again and each number that is positive - we know we never saw that index and we can add it to res

"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums:
            position = abs(i) - 1
            if nums[position] > 0:
                nums[position] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
