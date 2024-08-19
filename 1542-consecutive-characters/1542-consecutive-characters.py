class Solution:
    def maxPower(self, s: str) -> int:

        left , right = 0, 0
        maximum = 0
        count = 0

        while right < len(s):
            if s[left] == s[right]:
                count = count + 1
                maximum = max(count, maximum)
                right += 1
                
            else:
                count -= 1
                left = left + 1
     
            
        
        return maximum 