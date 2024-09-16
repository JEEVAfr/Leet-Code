class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        product = 1
        sum_digit = 0

        while n != 0:

            digit = int(math.fmod(n, 10))
            n = int(n / 10)

            product *= digit
            sum_digit += digit
        
        return product - sum_digit

        