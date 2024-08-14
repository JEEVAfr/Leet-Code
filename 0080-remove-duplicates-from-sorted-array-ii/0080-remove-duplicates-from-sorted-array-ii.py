class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count = count + 1
            else:
                count = 1
            
            if count <= 2:
                nums[left] = nums[i]
                left = left + 1
            
        return left