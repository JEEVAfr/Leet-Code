class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            
            s = nums[left] + nums[right]
            
            max_sum = max(max_sum, s)

            left = left + 1
            right = right - 1

        return max_sum
        


        