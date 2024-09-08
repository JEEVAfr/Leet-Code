class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        count_1 = 0
        count_2 = 0

        for i in nums1:
            if i in nums2:
                count_1 = count_1 + 1
        
        for j in nums2:
            if j in nums1:
                count_2 = count_2 + 1


        return [count_1, count_2]
        