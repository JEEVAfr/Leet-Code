class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left = 0
        right = 0

        while right < len(typed):

            if left < len(name) and name[left] == typed[right]:
                left = left + 1
            
            elif left == 0 or name[left - 1] != typed[right]:
                return False
            
            right = right + 1
        

        return left == len(name)
        

        