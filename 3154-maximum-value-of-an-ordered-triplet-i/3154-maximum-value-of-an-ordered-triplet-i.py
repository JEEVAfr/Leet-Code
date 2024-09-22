class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        max_sum = 0

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    a = ((nums[i] - nums[j]) * nums[k])
                    max_sum = max(a, max_sum)
        
        return max_sum

        