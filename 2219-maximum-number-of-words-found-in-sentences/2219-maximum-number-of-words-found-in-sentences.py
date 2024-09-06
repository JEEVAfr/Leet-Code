class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        maximum = 0

        for i in sentences:

            length = len(i.split())
            maximum = max(maximum, length)

        return maximum 

            
        