class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                l = j + 1
                r = n - 1
                while l < r:
                    c = nums[l]
                    d = nums[r]

                    s = nums[i] + nums[j] + c + d

                    if s > target:
                        r = r - 1
                    elif s < target:
                        l = l + 1
                    else:
                        result.add((nums[i], nums[j], c, d))
                        l = l + 1
                        r = r - 1

        return result             