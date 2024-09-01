class Solution:
    def pivotInteger(self, n: int) -> int:
        
        total_sum = n * (n + 1) // 2
        current_sum = 0

        for i in reversed(range(n + 1)):
            
            current_sum = current_sum + i

            if current_sum == total_sum:
                return i
            
            
            total_sum = total_sum - i
        

        return -1