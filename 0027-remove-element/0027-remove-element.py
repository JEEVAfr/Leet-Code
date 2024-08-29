class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left = left + 1
        
        return left
            