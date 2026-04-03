from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        currSum = 0
        counter = 0
        prefixMod = {0: 1}

        for num in nums:
            currSum += num
            mod = currSum % k
            counter += prefixMod.get(mod, 0)
            prefixMod[mod] = prefixMod.get(mod, 0) + 1

        return counter