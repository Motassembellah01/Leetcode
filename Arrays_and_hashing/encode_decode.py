from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        words_joint = ""
        for word in strs:
            words_joint += str(len(word)) + "#" + word
        return words_joint


    def decode(self, s: str) -> List[str]:
        list_words = []
        word = ""
        num_digits = 0
        i = 0
        j = 0
        while i < len(s) :
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            word = s[j+1: j+1+length]
            list_words.append(word)
            i = j + 1 + length
            j = i
            
        return list_words