class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_s = Counter(arr)

        a = set()
        for key, value in count_s.items():
            if value in a:
                return False
            a.add(value)
        
        return True
        