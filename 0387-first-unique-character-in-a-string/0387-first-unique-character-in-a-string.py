class Solution:
    def firstUniqChar(self, s: str) -> int:

        #dictinary
        count = {}

        for i in s:
            count[i] = count.get(i, 0) + 1

        # j -> index, char ->letter
        for j, char in enumerate(s):
            if count[char] == 1:
                return j
        

        return -1