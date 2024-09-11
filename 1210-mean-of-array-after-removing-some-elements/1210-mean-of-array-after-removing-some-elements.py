class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr.sort()

        n = len(arr)

        k = int(n * 0.05)

        arr = arr[k:]
        arr = arr[:-k]

        count = 0
        total = 0

        for i in arr:

            total = total + i
            count += 1
        
        b = (total / count)

        return b


        