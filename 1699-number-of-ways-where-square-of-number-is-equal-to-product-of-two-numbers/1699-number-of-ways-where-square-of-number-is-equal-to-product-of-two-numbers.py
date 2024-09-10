class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        map_1 = Counter([n * n for n in nums1])
        map_2 = Counter([n * n for n in nums2])

        res = 0

        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                res += map_2[nums1[i] * nums1[j]]


        
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                res += map_1[nums2[i] * nums2[j]]
        
        return res


        