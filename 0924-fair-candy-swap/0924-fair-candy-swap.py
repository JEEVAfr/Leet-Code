class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        a = sum(aliceSizes)
        b = sum(bobSizes)
        diff = (a - b)
        d = diff // 2

        bob = set(bobSizes)

        for i in aliceSizes:
            if (i - d) in bob:
                return [i, i - d]
            
        return []



        