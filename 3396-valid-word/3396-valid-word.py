class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3:
            return False
        elif re.search ("[^0-9a-zA-Z]", word):
            return False
        v = re.search("[aeiouAEIOU]", word)

        c = re.search("[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]",word)

        if v and c:
            return True
        else:
            return False