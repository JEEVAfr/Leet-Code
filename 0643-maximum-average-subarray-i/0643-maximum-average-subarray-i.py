class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        total = sum(nums[left:right])
        result = total
        

        while right < len(nums):

            result = result - nums[left] + nums[right]

            if result > total:
                total = result

            left = left + 1
            right = right + 1

        return total / k

        