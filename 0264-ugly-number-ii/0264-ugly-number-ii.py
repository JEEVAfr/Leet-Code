class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_number_list = [1]

        two_number = 0
        three_number = 0
        five_number = 0

        while len(ugly_number_list) < n: # ugly_number_list is equal to n it will break the loop

            by2 = ugly_number_list[two_number] * 2
            by3 = ugly_number_list[three_number] * 3
            by5 = ugly_number_list[five_number] * 5

            minimum = min(by2, by3, by5)
            ugly_number_list.append(minimum)

            if minimum == by2:
                two_number += 1
            if minimum == by3:
                three_number += 1
            if minimum == by5:
                five_number += 1
            
        return ugly_number_list[-1]


            


      