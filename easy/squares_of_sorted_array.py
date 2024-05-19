# Intuition - don't sort it first and then compute squares because remember sorting takes O(n(logn)), compute first and use reverse 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums)-1
        result = []

        while left_pointer <= right_pointer:
            if nums[left_pointer] * nums[left_pointer] > nums[right_pointer] * nums[right_pointer]:
                ans = nums[left_pointer] ** 2
                result.append(ans)
                left_pointer = left_pointer + 1
            else:
                ans = nums[right_pointer] ** 2
                result.append(ans)
                right_pointer = right_pointer - 1
        return result[::-1]
