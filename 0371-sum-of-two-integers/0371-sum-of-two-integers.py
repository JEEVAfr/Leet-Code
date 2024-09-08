class Solution:
    def getSum(self, a, b): 

        mask = 0xffffffff
        MAX  = 0x7FFFFFFF
         
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b)  & mask
            b = (carry << 1) & mask

        if a > MAX:
            a = ~(a ^ mask)
        
        return a 
        
 
	  
        