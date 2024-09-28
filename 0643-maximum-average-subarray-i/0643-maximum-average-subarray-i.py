class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left = 0
        right = 0

        current_sum = 0

        max_num = float('-inf')


        while right < len(nums):

            current_sum += nums[right]

            if right - left +  1 < k:
                right += 1
            
            else:
                max_num = max(current_sum, max_num)
                current_sum -= nums[left]
                left += 1
                right += 1
        
        return max_num / k
        
        