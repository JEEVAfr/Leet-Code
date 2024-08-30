class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
  
        even = 0
        odd = 1

        while even < len(nums) and odd < len(nums):

            if nums[even] % 2 == 0:
                even = even + 2

            elif nums[odd] % 2 == 1:
                odd = odd + 2
            
            else:
                nums[odd], nums[even] = nums[even], nums[odd]
                even = even + 2
                odd = odd + 2
        
        return nums

            
            

        