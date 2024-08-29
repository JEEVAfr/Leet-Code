class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        a = {}

        for i, num in enumerate(numbers):
            diff = target - num

            if diff in a:
                return [a[diff] + 1, i + 1]
            
            else:
                a[num] = i
                    
