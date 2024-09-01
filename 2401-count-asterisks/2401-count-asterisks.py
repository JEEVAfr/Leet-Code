class Solution:
    def countAsterisks(self, s: str) -> int:
        pair = False
        count = 0

        for i in s:
            # pair was False, it becomes True
            # pair was True, it becomes False
            if i == "|":
                pair = not pair
            elif i == "*" and not pair:
                count = count + 1
        
        return count


        