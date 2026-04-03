class Solution:
    def reverseWords(self, s: str) -> str:
        myArray = s.split()
        myArray.reverse()
        myString = ' '.join(myArray)
        return myString