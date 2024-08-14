class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        checking_pointer = 0

        while checking_pointer <= right:
            if nums[checking_pointer] == 0:
                nums[checking_pointer], nums[left] = nums[left], nums[checking_pointer]
                left = left + 1
                checking_pointer = checking_pointer + 1
            
            elif nums[checking_pointer] == 2:
                nums[checking_pointer], nums[right] = nums[right], nums[checking_pointer]
                right = right - 1
            
            elif nums[checking_pointer] == 1:
                checking_pointer = checking_pointer + 1
        