class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        s = set(nums)

        for i in s:
            if nums.count(i) > 2:
                return False
        
        return True

        

        

        