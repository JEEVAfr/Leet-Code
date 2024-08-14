class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        left = m - 1
        right = n - 1
        cp = (n + m) - 1
        
        while right >= 0:

            if left >= 0 and nums1[left] > nums2[right]:
                nums1[cp] = nums1[left]
                left = left - 1

            else: 
                nums1[cp] = nums2[right]
                right = right - 1

            cp = cp - 1
                
    

            



        