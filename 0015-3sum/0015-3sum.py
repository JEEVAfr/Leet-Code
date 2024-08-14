class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            a = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                b  = nums[j]
                c = nums[k]

                s = a + b + c 
                
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    triplets.add((a , b ,c))
                    j += 1
                    k -= 1
        return triplets
                