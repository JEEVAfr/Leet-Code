class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        count = 0
        left = 0
        right = 0

        while left < len(startTime) and right < len(endTime):

            if startTime[left] <= queryTime <= endTime[right]:
                count += 1
                left = left + 1
                right = right + 1
            
            else:
                left = left + 1
                right = right + 1
        
        return count

            

        