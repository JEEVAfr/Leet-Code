class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num % 2 != 0:
            return False
        
        total = 0

        for i in range(1, num// 2+ 1):
            if num % i == 0:
                total = total + i
            
        return num == total
            

        