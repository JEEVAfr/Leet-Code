class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        res = 0
        res_1 = 0

        for i in nums:
            res += i
        
        for i in nums:
            digit = sum(int(j) for j in str(i))
            res_1 += digit
            
        return res - res_1
        