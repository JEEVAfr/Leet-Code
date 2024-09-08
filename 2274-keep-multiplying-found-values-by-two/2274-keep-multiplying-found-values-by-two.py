class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        a = set(nums)
 

        while original in a:
            original = 2 * original
        
        return original
        
        

        