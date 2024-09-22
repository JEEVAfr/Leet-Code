class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w = max(nums)
        nums.remove(w)
        x = max(nums)
        nums.remove(x)

        y = min(nums)
        nums.remove(y)
        z = min(nums)
        nums.remove(z)

        return ((w*x)-(y*z))



