from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))
            hashMap[sorted_word].append(word)
        
        return list(hashMap.values())


# Better time complexity solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(m * n)
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter.lower()) - ord("a")] += 1
            res[tuple(count)].append(word)
        
        return list(res.values())

