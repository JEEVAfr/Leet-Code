class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result = [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                if result[0] == -1:  # If the first occurrence is not set, set it
                    result[0] = i
                result[1] = i  # Update the last occurrence to the current index

        return result

        
