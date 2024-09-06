class Solution:
    def countValidWords(self, sentence: str) -> int:

        s = sentence.split()
        
        pattern = r"^[a-z]+(-[a-z]+)?[!.,]?$|[!,.]$"

        count = 0
        
        for i in s:

            if re.match(pattern, i):
                count = count + 1

        return count
        