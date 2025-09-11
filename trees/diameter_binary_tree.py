from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_diameter

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)

        self.max_diameter = max(self.max_diameter, left_depth + right_depth)
        
        return 1 + max(left_depth, right_depth)