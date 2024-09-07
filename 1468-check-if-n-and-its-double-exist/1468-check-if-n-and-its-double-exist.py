class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        a = set()

        for i in arr:

            if 2 * i in a:
                return True

            if i % 2 == 0 and i // 2 in a:
                return True
            
            a.add(i)
        
        return False
        

        