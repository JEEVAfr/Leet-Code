class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        right = 0
        result = []
        count = 0

        while right < len(nums):
            count = count + nums[right]

            while count >= target:
                result.append(right - left + 1)
                count = count - nums[left]
                left = left + 1

            right = right + 1

        return 0 if len(result) == 0 else min(result)