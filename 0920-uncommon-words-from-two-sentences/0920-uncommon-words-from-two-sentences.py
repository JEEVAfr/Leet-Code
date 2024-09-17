class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        s1 = s1.split()
        s2 = s2.split()

        s = s1 + s2

        count = {}
        res = []

        for i in s:
            count[i] = count.get(i, 0) + 1
        
        for key, value in count.items():
            if value == 1:
                res.append(key) 

        
        return res


        