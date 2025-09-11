from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        def dfs(i):
            if i == len(nums):
                output.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return output

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]] 
        for num in nums:
            new_subs = []
            for sub in output:
                sub_copy = sub.copy()
                sub_copy.append(num)
                new_subs.append(sub_copy)
            for new_sub in new_subs:
                output.append(new_sub)
        return output

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            newSub = []
            for subset in res:
                newSub.append(subset + [num])
            res += newSub[:] 
        return res