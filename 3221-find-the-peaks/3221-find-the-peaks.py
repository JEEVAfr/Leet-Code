class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
       # If nums[i] > num[i - 1] and nums[i] > nums[i + 1] nums[i] is a peak.

        result = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                result.append(i)
        
        return result
        


            


        