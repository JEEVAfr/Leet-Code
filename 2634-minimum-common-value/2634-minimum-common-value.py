class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = 0
        result = []
        
        while left < len(nums1) and right < len(nums2):

            if nums1[left] == nums2[right]:
                result.append(nums1[left])
                right = right + 1
                left = left + 1

            
            elif nums1[left] < nums2[right]:
                left =left +  1
            else:
                right = right + 1
            
            

        return min(result) if result else -1
        