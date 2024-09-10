class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        pair = []

        i = 0

        while i < len(nums) - 1:

            if nums[i] == nums[i + 1]:
                pair.append((nums[i], nums[i + 1]))
            
            else:
                return False
            
            i += 2
        
        return True
        