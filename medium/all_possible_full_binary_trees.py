"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
 

Constraints:

1 <= n <= 20

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        def dfs(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            
            ans = []

            for nodes_in_left_subtree in range(n-1):
                nodes_in_right_subtree = n - 1 - nodes_in_left_subtree

                left_tree = dfs(nodes_in_left_subtree)
                right_tree = dfs(nodes_in_right_subtree)

                for left in left_tree:
                    for right in right_tree:
                        ans.append(TreeNode(0, left, right))
            return ans
        return dfs(n)