class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        nums = []

        for i in range(n):
            nums.append(start + 2 * i)

        unique = 0

        for i in nums:
            unique = unique ^ i
        
        return unique
        