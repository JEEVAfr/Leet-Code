class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        count = 0
        left = 0

        for i in range(len(s)):
            while s[i] in result:
                result.remove(s[left])
                left = left + 1
            result.add(s[i])
            count = max(count, i - left + 1)
        
        return count
        