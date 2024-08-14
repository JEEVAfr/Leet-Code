class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1 # start with 1

        for check_pointer in range(1, len(nums)): # iterate through the loop from 1 to len(nums)
            if nums[check_pointer] != nums[check_pointer - 1]: # if nums[right] is not equal to nums[right - 1] previous
                nums[left] = nums[check_pointer] # nums[left] is assign nums[right]
                left = left + 1  # increment left by 1 
        
        return left # return left

        



        

             
                
