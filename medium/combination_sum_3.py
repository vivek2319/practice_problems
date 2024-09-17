"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, summ):
            if summ > n or len(sol) > k:
                return
            if summ == n and len(sol) == k:
                ans.append(sol.copy())
                return
            
            for i in range(start, 10):
                sol.append(i)
                dfs(i+1, i + summ)
                sol.pop()
            

        sol = []
        ans = []
        dfs(1,0)

        return ans
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, summ):
            if summ > n or len(sol) > k:
                return
            if summ == n and len(sol) == k:
                ans.append(sol.copy())
                return
            
            for i in range(start, 10):
                sol.append(i)
                dfs(i+1, i + summ)
                sol.pop()
            

        sol = []
        ans = []
        dfs(1,0)

        return ans
