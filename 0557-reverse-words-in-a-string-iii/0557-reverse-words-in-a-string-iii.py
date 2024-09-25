class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        for word in s:
            # if self.reverse_word(word):
            res.append(self.reverse_word(word))
        
        return " ".join(res)

    

    def reverse_word(self, word):

        word = list(word)
        left = 0
        right = len(word) - 1

        while left < right:

            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        return "".join(word) 
    
        