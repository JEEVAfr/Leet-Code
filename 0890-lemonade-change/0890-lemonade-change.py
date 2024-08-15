class Solution:
    def lemonadeChange(self, bills: List[int]):
        five = 0
        ten = 0

        for i in bills:
            if i == 5:
                five = five + 1
            elif i == 10:
                ten = ten + 1
            
            change = i - 5

            if change == 5:
                if five > 0:
                    five = five - 1
                else:
                    return False
                
            elif change == 15:
                if five > 0 and ten > 0:
                    five = five - 1
                    ten = ten - 1
                elif five >= 3:
                    five = five - 3
                else:
                    return False
                
        return True