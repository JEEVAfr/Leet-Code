class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        left = 0
        right = 0

        while left < len(nums1) and right < len(nums2):

            if nums1[left] == nums2[right]:
                result.append(nums1[left])
                left = left + 1
                right = right + 1
            elif nums1[left] > nums2[right]:
                right = right + 1
            else:
                left = left + 1
        
        return result

