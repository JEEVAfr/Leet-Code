class Solution:
    def findLucky(self, arr: List[int]) -> int:

        count = {}
        
        for i in arr:
            count[i] = count.get(i, 0) + 1
        
        maximum = -1

        for key, value in count.items():
            if key == value:
                maximum = max(maximum, key)
        
        return maximum



        