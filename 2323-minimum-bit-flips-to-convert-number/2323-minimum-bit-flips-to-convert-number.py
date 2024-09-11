class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0

        while start or goal:

            if (start % 2) != (goal % 2): # goal % 2 either be 0 or 1
                res += 1
            
            start = start // 2
            goal = goal // 2
        
        return res
        