class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = {}
        count_t = {}
        
        for i in s:
            count_s[i] = count_s.get(i, 0) + 1
        
        for j in t:
            count_t[j] = count_t.get(j, 0) + 1

        for k in count_t:
            if count_t[k] != count_s.get(k, 0):
                return k



        
        