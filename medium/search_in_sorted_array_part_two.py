"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104

"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)  # size of the array
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            # if mid points to the target
            if nums[mid] == target:
                return True

            # Edge case:
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
                
            # if left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    # element exists
                    high = mid - 1
                else:
                    # element does not exist
                    low = mid + 1
            else:  # if right part is sorted
                if nums[mid] <= target <= nums[high]:
                    # element exists
                    low = mid + 1
                else:
                    # element does not exist
                    high = mid - 1

        return False

        
        
