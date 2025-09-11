from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]
                if value == ".":
                    continue
                elif value in rows[r] or value in cols[c] or value in grids[(r // 3, c // 3)]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                grids[(r // 3, c // 3)].add(value)
        return True