import collections
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        TREASURE = 0
        WATER = -1
        INF = 2**31 - 1

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = collections.deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == TREASURE:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS)
                    and (nr, nc) not in visit and grid[nr][nc] != WATER):
                        q.append((nr, nc))
                        visit.add((nr, nc))

            dist += 1