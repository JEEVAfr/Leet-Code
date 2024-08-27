class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0

        n = len(nums)

        for i in range(1, n + 1):
            if n % i == 0:
                a = nums[i - 1] * nums[i - 1]
                res = res + a
        
        return res


        