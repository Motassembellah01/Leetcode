class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        firstCount = {}
        secondCount = {}
        for i in range(len(s)):
            firstCount[s[i]] = firstCount.get(s[i], 0) + 1
            secondCount[t[i]] = secondCount.get(t[i], 0) + 1

        return firstCount == secondCount

# Another solution (Array)

class Solution:

    def counting(self, word: str):
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord("a")] += 1
        return count

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        firstCount = self.counting(s)
        secondCount = self.counting(t)
        return firstCount == secondCount