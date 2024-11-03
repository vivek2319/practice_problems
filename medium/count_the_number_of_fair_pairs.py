"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109

"""

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        N = len(nums)

        # Helper function to count pairs with sums <= target
        def count_pairs_with_sum_less_equal(target):
            left, right = 0, N - 1
            count = 0

            while left < right:
                if nums[left] + nums[right] <= target:
                    # All pairs from (left, left+1) to (left, right) are valid
                    count = count + right - left
                    left = left + 1
                else:
                    right = right - 1

            return count

        # Count pairs with sums <= upper and subtract pairs with sums < lower
        count = count_pairs_with_sum_less_equal(upper) - count_pairs_with_sum_less_equal(lower - 1)
        return count
