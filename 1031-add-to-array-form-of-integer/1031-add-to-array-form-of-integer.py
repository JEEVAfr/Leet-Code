class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(100000)
        result = []
        d = []

        for i in num:
            result.append(str(i))
        
        a = int("".join(result))

        c = a + k

        for j in str(c):
            d.append(int(j))
        
        return d


        
        