class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf') # this is larger value

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:

                s = a + nums[j] + nums[k]

                if abs(s - target) < abs(result - target):
                    result = s

                if s == target:
                    return s
                elif s > target:
                    k = k - 1
                else:
                    j = j + 1

        return result

        




                
  

        
        