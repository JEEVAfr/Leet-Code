class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left <= right:

            m = (left + right) // 2

            if nums[m] == m:
                left = m + 1 

            elif nums[m] != m:
                right = m - 1
            
        
        return left
             