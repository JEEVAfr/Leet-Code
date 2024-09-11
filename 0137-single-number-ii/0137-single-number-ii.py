class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        s = set(nums)

        sum_dis = sum(s) * 3
        a = sum(nums)

        result = (sum_dis - a) // 2

        return result