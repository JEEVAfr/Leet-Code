class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        result = ""

        left = 0
        right = 0

        while left < len(word1) and right < len(word2):

            if word1[left] > word2[right]:
                result = result + word1[left]
                left = left + 1

            
            elif word1[left] < word2[right]:
                result = result + word2[right]
                right = right + 1

            else:
                # word1 starting from index left to the end of the string.
                # word2 starting from index right to the end of the string.
                if word1[left:] > word2[right:]:
                    result = result + word1[left]
                    left = left + 1
                else:
                    result += word2[right]
                    right = right + 1

        # Append the remaining characters
        result = result + word1[left:]
        result = result + word2[right:]
        
        return result

            

        