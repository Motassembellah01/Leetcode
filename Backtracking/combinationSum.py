from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, total, sub):
            if i >= len(candidates) or total >= target:
                if total == target:
                    res.append(sub[:])
                return
            
            if total + candidates[i] > target:
                return

            sub.append(candidates[i])
            dfs(i, total + candidates[i], sub)
            sub.pop()
            dfs(i + 1, total, sub)

        dfs(0, 0, [])

        return res






