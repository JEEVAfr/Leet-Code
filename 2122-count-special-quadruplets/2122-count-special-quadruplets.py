class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
             for j in range(i + 1, len(nums)):
                for l in range(j + 1, len(nums)):
                    for k in range(l + 1, len(nums)):
                        if nums[i] + nums[j] + nums[l] == nums[k]:
                            count = count + 1
        
        return count