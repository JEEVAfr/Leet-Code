class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        l = 0
        r = 0
        
        while r < target or (r - target) % 2 != 0:
            l = l +  1
            r = r +  l
            
        return l

       