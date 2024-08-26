class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right + 1):
            a = str(i)
            if all(int(value) != 0 and i % int(value) == 0 for value in a):
                result.append(int(a))

        return result

        
            
                
        