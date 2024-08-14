class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        b = (map(lambda x : x[::-1], a))
        return " ".join(b)
    
        