class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        m = Counter(words1)
        n = Counter(words2)

        count = 0

        for i in words1:
            if m[i] == n[i] == 1:
                count += 1
        
        return count


        