class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        min_nums = float('inf')
        max_nums = 0

        for i in nums:
            if i < min_nums:
                min_nums = i
            
            diff = i - min_nums
            max_nums = max(max_nums, diff)
        
        return max_nums if max_nums else -1
      