class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        total = 0

        for i in arr1:

            left = bisect_left(arr2, i - d)
            right = bisect_right(arr2, i + d) - 1 # bisect_right and the -1 Adjustment
        
            if left > right:
                total = total + 1
        

        return total

 
        



        
        