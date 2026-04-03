
# Cleaner version
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        res = []
        count = 0

        for i in range(len(s) - 1, -1, -1):
            if count == k:
                res.append("-")
                count = 0
            res.append(s[i])
            count += 1

        return "".join(res[::-1])
    
# Older version
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        alphaNums = []
        
        for charac in s:
            if charac.isalnum():
                count += 1
                alphaNums.append(charac.upper())
                
        remain = count % k
        new_s = ""

        r = k if remain == 0 else remain
        for charac in alphaNums:
            if r == 0:
                new_s += "-"
                r = k - 1
            else:
                r -= 1
            new_s += charac
            
                
        return new_s