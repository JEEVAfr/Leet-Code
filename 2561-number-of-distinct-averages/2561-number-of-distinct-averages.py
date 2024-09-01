class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        a = set()
        

        while left < right : 
            average = (nums[left] + nums[right]) / 2

            if average not in a:
                a.add(average)
                
            
            left = left + 1
            right = right - 1

        return len(a)

            

        