class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = 0
        a = set(allowed)

        for i in words:
            if all(j in a for j in i):
                count += 1
        return count

        