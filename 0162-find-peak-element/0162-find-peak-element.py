class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2
            # peak element                          # # In case we find minimum:
            if nums[mid] < nums[mid + 1]:           # #if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return left # we call left or right


       
       
        