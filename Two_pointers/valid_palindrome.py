class Solution:
    def isAlphaNumeric(self, charac):
        isLowerCase = ord("a") <= ord(charac) <= ord("z")
        isUpperCase = ord("A") <= ord(charac) <= ord("Z")
        isDigit = ord("0") <= ord(charac) <= ord("9")

        return isLowerCase or isUpperCase or isDigit

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while l < r and not self.isAlphaNumeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True

