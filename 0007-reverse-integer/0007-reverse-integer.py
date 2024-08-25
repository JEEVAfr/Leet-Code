class Solution:

    def reverse(self, x: int) -> int:
        int_min = -2 ** 31 # value of (-2147483648)
        int_max = 2 ** 31 - 1 # value of (2147483647)

        result = 0

        while x:

            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (result > int_max // 10 or
                result == int_max // 10 and digit >= int_max % 10):
                return 0
            
            if (result < int_min // 10 or
                result == int_min // 10 and digit <= int_min % 10):
                return 0
            
            result = (result * 10) + digit

        return result









        
        
            