class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0

        for check_pointer in range(len(nums)):
            
            if nums[check_pointer] != 0:
                nums[check_pointer], nums[left] = nums[left], nums[check_pointer]
                left = left + 1
