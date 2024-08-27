class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))


        while left <= right:

            value = (left ** 2) + (right ** 2)

            if value == c:
                return True
            elif value > c:
                right = right - 1
            else:
                left = left + 1
        
        return False
        