class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        left = 0
        right = len(nums) - 1

        result = float('inf')

        while left < right:

            if nums[left] + nums[right]:
                average = (nums[left] + nums[right]) / 2
                result = min(result, average)
            left = left + 1
            right = right - 1
        
        return result
        