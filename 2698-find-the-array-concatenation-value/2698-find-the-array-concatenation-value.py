class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        value = 0

        while left < right:

            total = str(nums[left]) + str(nums[right])
            value = value + int(total)

            left = left + 1
            right = right - 1

        # After the loop, check if there's exactly one element left.

        if left == right:
            value = value + nums[left]  # You can also use nums[right] here.
        
        return value