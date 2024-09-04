"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return
            # Traverse the left sub-tree
            dfs(node.left)

            # process current and update diff
            nonlocal min_difference, prev_val
            min_difference = min(min_difference, node.val - prev_val)
            prev_val = node.val

            # Traverse the right sub-tree
            dfs(node.right)
        
        min_difference = float('inf')
        prev_val = float('-inf')
        
        # call the helper function and start from the root
        dfs(root)

        return min_difference
