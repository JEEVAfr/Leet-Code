class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            x = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:

                s = x + nums[l] + nums[r]

                if s == 0:
                    result.append([x, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while r > l and nums[r] == nums[r - 1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
                elif s > 0:
                    r = r - 1
                else:
                    l = l + 1
        
        return result

                