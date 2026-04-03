from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minim = float('inf')
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minim = min(minim, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if minim == float('inf') else minim