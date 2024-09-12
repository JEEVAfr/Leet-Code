class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = len(words)
        a = set(allowed)

        for i in words:
            for j in i:
                if j not in a:
                    count -= 1
                    break
        return count

        

        