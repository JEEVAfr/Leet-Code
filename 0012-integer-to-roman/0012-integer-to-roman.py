class Solution:
    def intToRoman(self, num: int) -> str:
        list_of_number = [["I", 1],["IV", 4], ["V", 5],["IX", 9],
                         ["X", 10],["XL", 40], ["L", 50],
                        ["XC", 90],["C", 100],["CD", 400],
                        ["D", 500],["CM", 900],["M", 1000]]

        result = ""

        for letter, value in reversed(list_of_number):
            if num // value:
                count = num // value
                result = result + (letter * count)
                num = num % value

            
        return result
        