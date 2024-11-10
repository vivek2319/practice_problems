"""
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b ), where: 
• Both subarrays nums [a ..a + k - 1] and nums [b ..b + k - 1] are strictly increasing. • The subarrays must be adjacent meaning b = a + k . Return t rue if it is possible to find two such subarrays, and false otherwise. A subarray is a contiguous non-empty sequence of elements within an array. 
Example 1: Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3 Output: t rue Explanation: • The subarray starting at index 2 is [7, 8, 9] , which is strictly increasing. • The subarray starting at index S is [2, 3, 4] , which is also strictly increasing. 


• The subarray starting at index 5 is [2, 3, 4] , which is also strictly increasing. • These two subarrays are adjacent, so the result is true.  Example 2: Input: nums = [1,2,3,4,4,4,4,5,6,7j, k = 5 Output: false 
Constraints: 
• 2 a nums.length <= 100 • 1 <= 2 * k <= nums.length • -1000 <= nums [1] <= 1000
"""
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2 * k:
            return False

        def is_strictly_increasing(start: int) -> bool:
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
    
        for i in range(n - 2 * k + 1):
            if is_strictly_increasing(i) and is_strictly_increasing(i + k):
                return True
    
        return False
