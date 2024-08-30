class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left = 0
        right = len(a) - 1

        while left <= right:
            if a[left] == a[right]:
                left = left + 1
                right = right - 1
            
            else:
                return False
        
        return True
 
        