class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        total = 0
        for i in range(len(arr1)):
            count = 0
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) > d:
                    count = count + 1
                else:
                    break
                
            if count == len(arr2):
                total = total + 1
            
        return total

        



        
        