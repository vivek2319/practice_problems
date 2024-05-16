"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result_dict = {}
        result = []

        for i in nums:
            if i in result_dict:
                result.append(i)
            else:
                result_dict[i] = 1
        return result
