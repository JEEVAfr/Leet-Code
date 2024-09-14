class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums
        
        res = 0

        for num in nums:
            result = set()
            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    result.add(num//i)
                    result.add(i)
                if len(result) > 4:
                    break
            
            if len(result) == 4:
                res += sum(result)

        return res
 


             
        