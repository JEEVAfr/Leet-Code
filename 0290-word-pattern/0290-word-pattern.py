class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        char_to_words = {}
        words_to_char = {}

        for c, word in zip(pattern, words):
            if c in char_to_words:
                if char_to_words[c] != word:
                    return False
            else:
                char_to_words[c] = word
            
            if word in words_to_char:
                if words_to_char[word] != c:
                    return False

            else:
                words_to_char[word] = c


        return True 

        

        