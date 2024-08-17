class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False

        count_a = {}
        count_b = {}

        for i in target:
            count_a[i] = count_a.get(i, 0) + 1

            
        for j in arr:
            count_b[j] = count_b.get(j, 0) + 1


        if count_a == count_b:
            return True
        else:
            return False
        