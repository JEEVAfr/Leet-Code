class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        if n >= 4:
            return False
        elif n == 1 or n == 2:
            return False
        

        