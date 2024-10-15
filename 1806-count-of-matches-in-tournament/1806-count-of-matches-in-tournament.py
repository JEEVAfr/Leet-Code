class Solution:
    def numberOfMatches(self, n: int) -> int:

        res = 0

        while n != 1:

            if n % 2 != 0:
                a = (n - 1) // 2
                res += a
                a += 1
            else:
                a = (n // 2)
                res += a
            
            n = a
        
        return res

        