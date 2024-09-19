class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        max_nums = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    max_nums = max(max_nums, diff)
        
        return max_nums if max_nums else -1
                