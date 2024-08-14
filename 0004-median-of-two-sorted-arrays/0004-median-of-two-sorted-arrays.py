class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        n = len(num)
        mid = n // 2

        if n % 2 == 0:
            median = (num[mid - 1] + num[mid]) / 2
            return median
        else:
            median = num[mid]
            return median

        