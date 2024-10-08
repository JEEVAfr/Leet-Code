class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        excepted = heights[:] # or a = list(heights) like copying
        heights.sort()
        count = 0

        for i in range(len(heights)):

            if heights[i] != excepted[i]:
                count += 1
        
        return count
        