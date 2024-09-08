class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        maximum = max(nums)

        for i in nums:

            if i != maximum:
                if maximum < 2 * i:
                    return -1
            
        return nums.index(maximum)
