class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left_pointer = 0
        for right_pointer in range(len(nums)):
            if nums[right_pointer]:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer = left_pointer + 1
        return nums
        
