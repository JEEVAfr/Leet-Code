class Solution:
    def repeatedCharacter(self, s: str) -> str:
        result = set()

        for i in s:
            if i not in result:
                result.add(i)
            else:
                return i


        