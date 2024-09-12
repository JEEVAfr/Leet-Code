class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        count = {}
        n = len(arr)
        k = int(n * 0.25)

        for i in arr:
            count[i] = count.get(i, 0) + 1
        
        for key, value in count.items():
            if value > k:
                return key

        