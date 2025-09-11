from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        for i, a in enumerate(nums):

            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1

        return res

    
        # Possible Brute force, but NOT PRACTICAL at all -> time complexity :(

        # nums.sort()
        # res = set()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             threeSum = nums[i] + nums[j] + nums[k]
        #             if threeSum == 0:
        #                 res.add(tuple([nums[i], nums[j], nums[k]]))
        
        # return [list(triplet) for triplet in res]
