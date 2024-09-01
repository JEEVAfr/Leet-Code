class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maximum = 0

        for i in accounts:
            total_sum = sum(i)
            maximum = max(maximum, total_sum)
        
        return maximum
        