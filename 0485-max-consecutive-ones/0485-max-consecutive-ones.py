class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0
        for i in nums:
            if i != 0:
                count = count + 1
                maximum = max(maximum, count)
            else:
                count = 0
            
        return maximum