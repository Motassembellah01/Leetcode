from typing import List

# Cleaner
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxIsland = 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            
            if (r, c) in visited or r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxIsland = max(maxIsland, dfs(r, c))

        return maxIsland

# this one also works
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxIsland = 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c, counter):
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols):
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        counter = dfs(nr, nc, counter + 1)
            
            return counter
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c, 1)
                    maxIsland = max(area, maxIsland)

        return maxIsland