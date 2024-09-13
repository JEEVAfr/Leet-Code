class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        a = set()
        res = []

        for i in nums:
            if i not in a:
                a.add(i)
            else:
                res.append(i)
        return res
        