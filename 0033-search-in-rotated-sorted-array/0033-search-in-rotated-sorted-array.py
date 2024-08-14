class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left + right) // 2

            if nums[m] == target:
                return m
            
            elif nums[left] <= nums[m]:
                if nums[left] <= target <= nums[m]:
                    right = right - 1
                else:
                    left = left + 1
            
            else:
                if nums[m] <= target <= nums[right]:
                    left =left + 1
                else:
                    right = right - 1
            
            
        return -1
        