class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf') # Assume this as largest possible integer. 

        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            max_profit = max(max_profit, profit)
        
        return max_profit


        