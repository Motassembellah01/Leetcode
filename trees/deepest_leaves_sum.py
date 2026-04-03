# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

from trees.balanced_binary_tree import TreeNode

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # BFS OPTIMIZED 
        if not root:
            return 0

        next_level = deque([root])
        while next_level:
            curr_level = next_level
            next_level = deque()

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        
        return sum(node.val for node in curr_level)