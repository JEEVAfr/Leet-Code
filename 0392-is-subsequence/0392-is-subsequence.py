class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        left = 0  # start with zero
        right = 0 # start with zero

        while left < len(s) and right < len(t): # check 0 < 3 and 0 < 5:

            if s[left] == t[right]:   
                left = left + 1         # s[left] equals t[right], we increment left by 1.
            right = right + 1   # s[left] is not equal to t[right] we only increment right by 1.                            
           
        
        return left == len(s)  # True
        