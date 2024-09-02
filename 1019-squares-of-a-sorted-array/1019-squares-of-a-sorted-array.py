class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        index = len(nums) - 1

        while left <= right:

            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                res[index] = left_sq
                left = left + 1

            else:
                res[index] = right_sq
                right = right - 1
        
            index = index - 1

        return res