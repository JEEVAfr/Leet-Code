class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        left = 0
        right = k
        result = 0

        vowel = ["a", "e", "i", "o", "u"]
        
        for i in s[left:right]:
            if i in vowel:
                result += 1

        max_count = result
        
        while right < len(s):

            if s[left] in vowel:
                result -= 1
            if s[right] in vowel:
                result += 1
            
            max_count = max(max_count, result)

            left += 1
            right += 1
        
        return max_count