class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        a = {}
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = len(nums) - 1

                while l < r:

                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        while r < l and nums[r] == nums[r - 1]:
                            r = r - 1

                        l = l + 1
                        r = r - 1
                    
                    elif s > target:
                        r = r - 1
                    else:
                        l = l + 1
        
        return result



                 
        
        