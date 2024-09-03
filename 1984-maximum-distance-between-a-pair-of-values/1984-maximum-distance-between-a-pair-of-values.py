class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        max_dist = 0

        left = 0
        right = 0

        while left < len(nums1) and right < len(nums2):

            if nums1[left] <= nums2[right]:
                max_dist = max(max_dist, right - left)
                right = right + 1
            
            # nums1[left] >= nums2[right]
            else:
                left = left + 1
            
        return max_dist if max_dist else 0
        

        