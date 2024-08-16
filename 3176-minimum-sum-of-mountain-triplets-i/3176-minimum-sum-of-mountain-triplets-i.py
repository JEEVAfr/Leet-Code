class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        total =  1000000

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] < nums [j]) and (nums[k] < nums[j]) :
                        a = nums[i] + nums[j] + nums[k]
                        if total > a:
                            total = a

        return total if total != 1000000 else -1
        