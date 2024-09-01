class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        if len(nums) < 2:
            return [0, 0] if indexDifference == 0 and valueDifference == 0 else [-1, -1]

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
            
        return [-1, -1]


        