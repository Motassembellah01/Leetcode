from typing import List

# Top Down
class Solution:
    def easyRob(self, nums: List[int]) -> int:
        
        prev_two = 0
        prev_one = 0

        for money in nums:
            best_now = max(money + prev_two, prev_one)
            prev_two = prev_one
            prev_one = best_now

        return prev_one

    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(self.easyRob(nums[:- 1]), self.easyRob(nums[1:]))

# Bottom Up

class Solution:
    def easyRob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(self.easyRob(nums[:- 1]), self.easyRob(nums[1:]))

# [1, 2, 3, 1]

# [2, 3, 1]

# [1, 2, 3]

        