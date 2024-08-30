class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        result = 0

        while x:

            digit = math.fmod(x, 10)
            x = x // 10

            result = (result * 10) + digit

    
        return original == result        