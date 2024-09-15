"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        sol = [0] * n
        visited = [False] * n

        def dfs(i):
            if i == n:
                res.append(sol.copy())
                return
            
            for j in range(n):
                if visited[j] or (j > 0 and nums[j] == nums[j-1] and not visited[j-1]):
                    continue
                sol[i] = nums[j]
                visited[j] = True
                dfs(i+1)
                visited[j] = False 
            
        
        dfs(0)
        return res
