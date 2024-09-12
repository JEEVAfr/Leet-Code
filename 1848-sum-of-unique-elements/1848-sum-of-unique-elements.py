class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        total = 0

        for key, value in count.items():
            if value <= 1:
                total += key
        
        return total


        