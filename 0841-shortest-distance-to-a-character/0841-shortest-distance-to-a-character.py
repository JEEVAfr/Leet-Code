class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        for i in range(len(s)):
            if s[i] == c:
                result.append(i)

        result_1 = []

        for i in range(len(s)):
            result_1.append(min([abs(j - i) for j in result]))

        return result_1

        

        