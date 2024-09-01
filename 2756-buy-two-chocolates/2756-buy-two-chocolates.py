class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()
        
        num = money

        for i in range(2):

            num = num - prices[i]

            if num < 0:
                return money
        
        return num