class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()

        left = 0
        right = k

        current_sum = 0
        min_sum = 2 ** 31 - 1

        while right <=  len(nums):

            current_sum = nums[right - 1] - nums[left]

            min_sum = min(current_sum, min_sum)

            left += 1
            right += 1
        
        return min_sum
        