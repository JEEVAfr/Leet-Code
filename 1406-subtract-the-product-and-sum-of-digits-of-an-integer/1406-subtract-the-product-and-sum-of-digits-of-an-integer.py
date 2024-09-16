class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        product = 1
        sum_digit = 0

        for i in str(n):

            product *= int(i)
            sum_digit += int(i)
        
        return product - sum_digit
        