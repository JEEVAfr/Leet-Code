class Solution:
    def minimumSteps(self, s: str) -> int:

        left = 0
        res = 0


        for r in range(len(s)):

            if s[r] == "0":
                res += (r - left)

                left += 1
        
        return res
        