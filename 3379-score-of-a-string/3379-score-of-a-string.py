class Solution:
    def scoreOfString(self, s: str) -> int:

        total = 0

        for i in range(len(s) - 1):

            a = abs(ord(s[i]) - ord(s[i + 1]))
            total = total + a
        
        return total