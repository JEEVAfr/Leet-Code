class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        max_zeros = 0
        left = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                max_zeros += 1
            
            while max_zeros > k:
                if nums[left] == 0:
                    max_zeros -= 1
                left += 1
            
            w = r - left + 1
            longest = max(longest, w)

        return longest                
        