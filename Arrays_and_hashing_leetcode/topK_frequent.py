from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        freq = [[] for i in range(len(nums) + 1)] 
        for number in nums:
            count[number] = count.get(number, 0) + 1

        for number, numberOccurences in count.items():
            freq[numberOccurences].append(number)

        for i in range(len(freq) - 1, 0, -1):
            if freq[i] != []:
                for number in freq[i]:
                    res.append(number)
                    if len(res) == k:
                        return res
        return res


