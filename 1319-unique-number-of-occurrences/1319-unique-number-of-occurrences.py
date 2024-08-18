class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_s = {}

        for i in arr:
            count_s[i] = count_s.get(i, 0) + 1 

        a = set()
        for key, value in count_s.items():
            if value in a:
                return False
            a.add(value)
        
        return True
        