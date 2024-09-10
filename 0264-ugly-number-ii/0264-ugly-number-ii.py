class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]

        i2, i3, i5 = 0, 0, 0
        
        for i in range(1, n): # while len(ugly_number_list) < n:

            minimum = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(minimum)

            if minimum == nums[i2] * 2:
                i2 += 1
            if minimum == nums[i3] * 3:
                i3 += 1
            if minimum == nums[i5] * 5:
                i5 += 1
            
        return nums[-1]


            


      