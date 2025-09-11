from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        numStairs = len(cost)

        for i in range(numStairs - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        memoiz = [-1] * n

        def dp(i):
            if i >= n:
                return 0

            if memoiz[i] == -1:
                memoiz[i] = cost[i] + min(dp(i + 1), dp(i + 2))

            return memoiz[i]

        return min(dp(0), dp(1))



