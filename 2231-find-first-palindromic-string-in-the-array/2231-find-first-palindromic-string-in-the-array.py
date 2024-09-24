class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        """
        for i in words:
            if i == i[::-1]:
                return i
        return ""
        """

        for word in words:
            if self.palindrome(word):
                return word
        return ""


    def palindrome(self,word):

        left = 0
        right = len(word) - 1

        while left <= right:

            if word[left] == word[right]:
                left += 1
                right -= 1
                
            else:
                return False
        
        return True

        