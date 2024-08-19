class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0
        for i in nums:
            if i != 0:
                count = count + 1
            else:
                maximum = max(maximum, count)
                count = 0
        
        return max(maximum, count)
        