class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            distance = right - left  # (right - left) - index 

            m = min(height[left], height[right]) # minimum of left and right

            f = distance * m

            result = max(result, f)

            if height[left] > height[right]:
                right = right - 1
            
            else:
                left = left + 1


        return result






        