class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numset1, numset2 = set(nums1), set(nums2)

        res1 , res2 = set(), set()
        for i in nums1:
            if i not in numset2:
                res1.add(i)
            
        for j in nums2:
            if j not in numset1:
                res2.add(j)
        
        return [list(res1), list(res2)]
        