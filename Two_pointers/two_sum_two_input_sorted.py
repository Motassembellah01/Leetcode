from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Better because I don't have to store! (O(1) for space, O(n) for time)
        l = 0
        r = len(numbers) - 1
        while l < r:
            my_sum = numbers[l] + numbers[r]
            if my_sum > target:
                r -= 1
            elif my_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
            
        
        # Same time complexity, but worst in space complexity (O(n) for space, O(n) for time)

        # hashMap = {}
        # for index, num in enumerate(numbers):
        #     difference = target - num
        #     if difference in hashMap:
        #         return [hashMap[difference] + 1, index + 1]
        #     hashMap[num] = index
        # return []