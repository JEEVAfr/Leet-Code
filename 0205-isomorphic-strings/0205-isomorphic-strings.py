class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map_s = [0] * 128
        map_t = [0] * 128

        for i in range(len(s)):

            index_s = ord(s[i])
            index_t = ord(t[i])

            if map_s[index_s] != map_t[index_t]:
                return False
            
            map_s[index_s] = i + 1
            map_t[index_t] = i + 1

        return True
        