class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums) // 2
        pair = []
        a = nums[:n]
        b = nums[n:] 

        left = 0
        right = 0
        
        while left < len(a) and right < len(b):

            if 2 * a[left] <= b[right]:
                pair.append((a[left], b[right]))
                left = left + 1
                right = right + 1

            else:
                right = right + 1
        
        return len(pair) * 2

