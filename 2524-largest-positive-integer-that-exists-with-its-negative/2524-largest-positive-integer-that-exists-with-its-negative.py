class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        result = []
        
        for i in nums:
            if i > 0 and -i in s:
                result.append(i)
            
        if result:
            return max(result)
        else:
            return -1



        
        