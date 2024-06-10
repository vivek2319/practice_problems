"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_number = self.bin_search(nums, target, True)
        right_number = self.bin_search(nums, target, False)
        return[left_number, right_number]

    def bin_search(self, nums, target, looking_for_left_num):
        index = -1
        left_pointer, right_pointer = 0, len(nums) - 1
        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            if target > nums[mid]:
                left_pointer = mid + 1
            elif target < nums[mid]:
                right_pointer = mid - 1
            else:
                index = mid
                if looking_for_left_num:
                    right_pointer = mid - 1
                else:
                    left_pointer = mid + 1
        return index
