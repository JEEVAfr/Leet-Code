class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        left = 0
        current_sum = 0
        max_sum = 0
        result = set()

        for right in range(len(nums)):

            while nums[right] in result:
                result.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            result.add(nums[right])
            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
            
                result.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        
        return max_sum
            

