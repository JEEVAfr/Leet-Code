class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                total += i
                count += 1

            if count == 0:
                result = 0
            else:
                result = math.floor(total / count)
        
        return result