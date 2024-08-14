class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        a = s + s 
        
        if len(s) != len(goal):
            return False

        for i in range(len(a)):
            if a[i: i + len(goal)] == goal:
                return True

        

        