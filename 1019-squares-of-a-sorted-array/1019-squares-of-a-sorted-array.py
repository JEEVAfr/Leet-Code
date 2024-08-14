class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = list(map(lambda i: i * i, nums))
        a.sort()
        return a