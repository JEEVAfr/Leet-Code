class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf') # this is larger value

        for i in range(len(nums) - 2):
            a = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:

                b = nums[j]
                c = nums[k]

                s = a + b + c

                if abs(s - target) < abs(result - target):
                    result = s

                if s == target:
                    return s
                elif s > target:
                    k = k - 1
                else:
                    j = j + 1

        return result

        




                
  

        
        