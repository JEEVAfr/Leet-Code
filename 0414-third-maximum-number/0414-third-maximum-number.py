class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m = set(nums)
        
        if len(m) < 3:
            return max(m)

        for i in range(3):
            n = max(m)
            m.remove(n)
        
        return n

        



        