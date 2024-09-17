class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        res = 0
        a = set(jewels)

        for i in stones:

            if i in a:
                res += 1
        
        return res
        