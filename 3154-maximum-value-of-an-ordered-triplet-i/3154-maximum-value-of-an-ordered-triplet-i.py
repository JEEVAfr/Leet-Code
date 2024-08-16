class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        value = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    a = ((nums[i] - nums[j]) * nums[k])
                    if value < a:
                        value = a
        
        return value

        