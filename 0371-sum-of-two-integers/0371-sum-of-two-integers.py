class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask
            
        # If a is negative, convert it to a Python negative integer
        if a > MAX:
            a = ~(a ^ mask)
            
        return a

         
	  
        