"""
Given an integer array nums , return the number of subarrays of length 3 such that the sum of the
first and third numbers equals exactly half of the second number.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [1,2,1,4,1]
Output: 1
Explanation:
Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third
numbers equals half the middle number.
Example 2:
Input: nums = [1,1,1]
Output: 0
 
Explanation:
(1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half
the middle number.
Constraints:
* 3 <= nums. length <= 100
* -168 <= nums[i] <= 100

"""

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            first = nums[i]
            second = nums[i+1]
            third = nums[i+2]
            if first + third == second / 2:
                count = count + 1

        return count
