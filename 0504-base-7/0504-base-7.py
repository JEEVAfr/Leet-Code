class Solution:
    def convertToBase7(self, num: int) -> str:

        x = abs(num)
        res = ""


        while x:

            digit = (x % 7)
            x = x // 7

            res = str(digit) + res
        
        if num < 0:
            res = "-" + res
        
        return res if res else "0"
        