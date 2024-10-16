class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        max_num = 0
        current_num = nums[0]

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                current_num += nums[i]

            else:
                max_num = max(current_num, max_num)
                current_num = nums[i]
        
        max_num = max(max_num, current_num)
        
        return max_num