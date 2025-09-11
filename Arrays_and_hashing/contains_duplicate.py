from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False



# Other Solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        return len(hashset) != len(nums)