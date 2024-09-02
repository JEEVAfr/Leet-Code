class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        left = 0
        right = 0

        count = 0

        while left < len(g) and right < len(s):

            if g[left] <= s[right]:
                count = count + 1
                left = left + 1
                right = right + 1
        
            else:
                right = right + 1

        return count