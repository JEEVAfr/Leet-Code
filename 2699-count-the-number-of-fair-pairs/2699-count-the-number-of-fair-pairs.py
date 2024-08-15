class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        value = 0

        while left < right:

            if nums[left] + nums[right] <= upper:
                value = value + right - left
                left = left + 1
            else:
                right = right - 1
            
        
        left = 0
        right = len(nums) - 1
        value_1 = 0
    

        while left < right:

            if nums[left] + nums[right] < lower:
                value_1 = value_1 + right - left
                left = left + 1

            else:
                right = right - 1



        return  abs(value - value_1)
                



        