from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sum = 1

        for number in nums:
            sum *= number
        
        if sum > 0:
            return 1

        elif sum < 0:
            return -1

        return 0
