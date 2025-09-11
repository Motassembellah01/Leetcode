from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:]) # n
        res = []

        for p in perms: # (n - 1)!
            for i in range(len(p) + 1): # n
                p_copy = p.copy()
                p_copy.insert(i, nums[0]) # n
                res.append(p_copy)
        
        return res

# This one is more iterative
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = [[]]
        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            perms = new_perms[:]

        return perms
