class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        a = set()
        count = 0

        while left < right : 
            average = (nums[left] + nums[right]) / 2

            if average not in a:
                a.add(average)
                count = count + 1
            
            left = left + 1
            right = right - 1

        return count

            

        