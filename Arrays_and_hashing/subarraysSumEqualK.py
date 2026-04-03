from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        counter = 0
        cumSum = 0
        prefixSums = {0: 1}

        for num in nums:
            cumSum += num
            diff = cumSum - k
            counter += prefixSums.get(diff, 0)
            prefixSums[cumSum] = prefixSums.get(cumSum, 0) + 1

        return counter

        