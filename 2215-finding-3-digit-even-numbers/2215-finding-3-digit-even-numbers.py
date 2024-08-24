class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_set = set()

        even = [0, 2, 4, 6, 8]

        for p in permutations(digits, 3):
            if p[2] in even:
                num = p[0] * 100 + p[1] * 10 + p[2] * 1
                if p[0] != 0:
                    unique_set.add(num)


        return sorted(unique_set)
