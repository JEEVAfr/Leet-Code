class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        nums = []

        for i in range(n):
            a = (start + 2 * i)
            nums.append(a)

        unique = 0

        for i in nums:
            unique = unique ^ i
        
        return unique
        