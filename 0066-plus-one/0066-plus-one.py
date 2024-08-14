class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        joined_string = ''.join(map(str, digits))
        a = int(joined_string)
        value = a + 1
        d = str(value)
        c = [int(char) for char in d]

        return c    
        