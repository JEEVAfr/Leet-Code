class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        res = 0

        a = text.split()
        b = set(brokenLetters)

        for i in a:
            if all(j not in b for j in i):
                res += 1
        
        return res
        