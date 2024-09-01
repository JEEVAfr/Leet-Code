class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowel = [ "a", "e", "i", "o", "u", "A", "E", "I", "O", "U" ]

        half = len(s) // 2

        first_half = s[:half]
        second_half = s[half:]

        count_first_half = 0
        count_second_half = 0

        for i in first_half:
            if i in vowel:
                count_first_half = count_first_half + 1
        
        for j in second_half:
            if j in vowel:
                count_second_half = count_second_half + 1
        

        return count_first_half == count_second_half

        