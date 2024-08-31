class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}

        for i in range(1, n + 1):
            digit = sum(int(digit) for digit in str(i))

            if digit in freq:
                freq[digit] += 1
            else:
                freq[digit] = 1
        
        size = max(freq.values())

        count = 0

        for i in freq.values():
            if i == size:
                count = count + 1
        
        return count



        