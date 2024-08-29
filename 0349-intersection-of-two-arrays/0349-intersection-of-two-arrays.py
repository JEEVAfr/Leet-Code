class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_1 = set(nums1)
        num_2 = set(nums2)

        result = set()
        for i in nums1:
            if i in num_2:
                result.add(i)
        
        return result
