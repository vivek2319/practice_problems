"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        # Recursive DFS
		# Using Prefix Sum approach
        
        def dfs(node, curr_sum, sum):
            if not node:
                return 0
            
            res = 0
            curr_sum += node.val
            
            if (curr_sum - sum) in mapping:
                res += mapping[curr_sum - sum]
            if curr_sum in mapping:
                mapping[curr_sum] += 1
            else:
                mapping[curr_sum] = 1
                
            res += dfs(node.left, curr_sum, sum)
            res += dfs(node.right, curr_sum, sum)
            mapping[curr_sum] -= 1
            
            return res
            
        mapping = defaultdict(int)
        mapping[0] = 1
        return dfs(root, 0, targetSum)
