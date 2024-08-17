class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a = Counter(target)
        b = Counter(arr)

        if a == b:
            return True
        else:
            return False