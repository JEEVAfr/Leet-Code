class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        english_letter = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        s = list(s)

        while left < right:
            if s[left] in english_letter and s[right] in english_letter:
                s[left], s[right] = s[right], s[left]
                left = left + 1
                right = right - 1
            
            elif s[left] not in english_letter:
                left = left + 1
            
            elif s[right] not in english_letter:
                right = right - 1

        return "".join(s)
                    
        



        