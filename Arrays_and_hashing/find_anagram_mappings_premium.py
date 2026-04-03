from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        solution = []
        for j, num in enumerate(nums2):
            hashMap[num] = j
        
        for i in range(len(nums1)):
            solution.append(hashMap[nums1[i]])

        return solution
