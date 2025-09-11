import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        output = []
        fringe = collections.deque([root])

        while fringe:
            level = []
            fringeSize = len(fringe)
            for i in range(fringeSize):
                curr = fringe.popleft()
                if curr:
                    level.append(curr.val)
                    fringe.append(curr.left)
                    fringe.append(curr.right)
            if level:
                output.append(level)
        
        return output
    


# DFS working BUT NOT practical here because we traverse by level so BFS more appropriate

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         # output = [[root.val]]
#         # DFS
#         levelsNodes = defaultdict(list)
#         # fringe = collections.deque([root])

#         def dfs(node: Optional[TreeNode], level):
#             if not node:
#                 return
            
#             levelsNodes[level].append(node.val)

#             dfs(node.left, level + 1)
#             dfs(node.right, level + 1)
        
#         dfs(root, 0)

#         return list(levelsNodes.values())

