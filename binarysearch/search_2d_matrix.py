from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            currRow = m // len(matrix[0])
            currCol = m % len(matrix[0])
            if matrix[currRow][currCol] < target:
                l = m + 1
            elif matrix[currRow][currCol] > target:
                r = m - 1
            else:
                return True
        return False