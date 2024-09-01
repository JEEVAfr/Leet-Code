class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        res = []

        for i in range(m):

            start = i * n
            print(start)
            end = start + n   #(start + n - 1)
            print(end)
            res.append(original[start:end])
        
        return res
        