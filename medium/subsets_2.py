"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(start_index, sol):
            res.append(sol.copy())
            
            for index in range(start_index, len(nums)):
                if index != start_index and nums[index] == nums[index-1]:
                    continue
                c = nums[index]
                sol.append(c)
                dfs(index+1, sol)
                sol.pop()

        nums.sort()
        res = []
        sol = []
        dfs(0, [])
        return res
