# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from trees.balanced_binary_tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0
            
            # Update the current sum
            current_sum += node.val
            
            # Count paths that sum to targetSum, which would be any previous path 
            # that had a cumulative sum of (current_sum - targetSum)
            count = prefix_sum.get(current_sum - targetSum, 0)
            
            # Update the prefix_sum with the current cumulative sum
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
            
            # Continue the DFS traversal with left and right children
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Backtrack: remove the current sum from the map to maintain correctness
            prefix_sum[current_sum] -= 1
            if prefix_sum[current_sum] == 0:
                del prefix_sum[current_sum]
            
            return count

        # HashMap to store cumulative sum frequencies
        prefix_sum = {0: 1}  # We start with a sum of 0 (base case)
        return dfs(root, 0)