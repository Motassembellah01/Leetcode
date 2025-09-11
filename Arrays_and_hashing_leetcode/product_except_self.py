from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my_list = [1, 2, 3, 4]
        # prefix -> [1, 1, 2, 6]
        # suffix -> [24, 12, 4, 1]
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
