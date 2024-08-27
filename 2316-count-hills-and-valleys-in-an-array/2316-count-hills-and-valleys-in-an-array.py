class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0
        
        count_hill = 0
        count_valley = 0

        cleaned_nums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != cleaned_nums[-1]:
                cleaned_nums.append(nums[i])


        for i in range(1, len(cleaned_nums) - 1):

            if (cleaned_nums[i] > cleaned_nums[i - 1] and cleaned_nums[i] > cleaned_nums[i + 1]):
                count_hill += 1
            elif cleaned_nums[i] < cleaned_nums[i - 1] and cleaned_nums[i] < cleaned_nums[i + 1]:
                count_valley += 1
                
        
        return count_hill + count_valley




        