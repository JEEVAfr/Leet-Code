class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        a = x
        total = 0

        while x:

            digit = x % 10
            total += int(digit)
            x = x / 10
        
        if a % total == 0:
            return total
        else:
            return -1
         
