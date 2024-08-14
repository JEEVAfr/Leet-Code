class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = re.sub(r'[^a-zA-Z0-9]', '', s)
        b = a.lower()

        left = 0
        right = len(b) - 1

        while left <= right:
            if b[left] == b[right]:
                left = left + 1
                right = right - 1
            
            else:
                return False
        
        return True
 
        