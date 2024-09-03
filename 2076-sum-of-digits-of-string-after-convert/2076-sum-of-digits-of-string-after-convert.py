class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        mapping = {letter : str(index + 1) for index, letter in enumerate(string.ascii_lowercase)}

        conversion = [mapping[c] for c in s]
        
        num = "".join(conversion)

        while k > 0:
            number = 0
            for i in num:
                number = number + int(i)
            num = str(number)
            k = k - 1
        
        return number
        



        