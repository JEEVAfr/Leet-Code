class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        res = 0
        n = str(n)
        for i in range(len(n)):
            
            if i % 2 == 0:
                res = res + int(n[i])
            else:
                res = res - int(n[i])
        
        return res