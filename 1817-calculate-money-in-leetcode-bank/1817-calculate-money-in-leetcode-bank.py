class Solution:
    def totalMoney(self, n: int) -> int:

        num_week = n // 7
        num_days = n % 7

        res = 0

        for i in range(1, num_week + 1):
            res += (7 * i + 21)
        
        for i in range(num_days):
            res += (num_week + 1 + i)

        return res
        