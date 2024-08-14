class Solution:
    def countElements(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)

        count = 0
        for num in nums:
            if minimum < num < maximum:
                count = count + 1
            
        return count

                
        
            
        