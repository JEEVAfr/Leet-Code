class Solution:
    def maxPower(self, s: str) -> int:

        count = 1
        maximum_count = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count = count + 1
                maximum_count = max(count, maximum_count)
            else:
                count = 1
            
        return maximum_count

