class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0 and n % n == 0:
            return n
        
        else:
            a = n / n 
            b = (a * n) * 2
            return int(b)
            
        