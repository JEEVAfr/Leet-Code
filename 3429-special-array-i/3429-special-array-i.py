class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pair = []

        for i in range(len(nums) - 1):

            if (nums[i] % 2 == 0)== (nums[i + 1] % 2 == 0):
                return False
        
        return True
        