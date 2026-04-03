# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from trees.balanced_binary_tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # An empty tree is symmetric
        
        # Compare the left and right subtrees
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        # If both nodes are None, they are symmetric
        if not left and not right:
            return True
        
        # If one is None and the other is not, they are not symmetric
        if not left or not right:
            return False
        
        # Compare current node values
        if left.val != right.val:
            return False
        
        # Recursively check if the left's left is symmetric with right's right
        # and left's right is symmetric with right's left
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)