# This is not what you think! You can't use dict, you need to read about 
# https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        item_set = set()

        for i in nums:
            if i in item_set:
                return i
            else:
                item_set.add(i)
