class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        maximum = 0
        minimum = 0

        for i in nums:

            if i < 0:
                minimum += 1
            elif i > 0:
                maximum += 1

        return max(maximum, minimum) 
        