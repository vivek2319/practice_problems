class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(nums) - 1
        
        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            if nums[mid] > target:
                right_pointer = mid - 1
            elif nums[mid] < target:
                left_pointer = mid + 1
            else:
                return mid
        return -1
