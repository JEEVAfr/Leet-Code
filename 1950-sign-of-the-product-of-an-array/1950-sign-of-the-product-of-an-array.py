class Solution:
    def arraySign(self, nums: List[int]) -> int:

        total = 1
        for i in nums:
            total *= i
        
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        
        return signFunc(total)
        