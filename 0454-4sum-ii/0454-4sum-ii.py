class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        count = 0 
        a = dict()

        # Store sums of nums1[i] + nums2[j] in a hash map
        for i in nums1:
            for j in nums2:
                s = i + j
                if s in a:
                    a[s] = a[s] + 1
                else:
                    a[s] = 1

        for i in nums3:
            for j in nums4:
                b = - (i + j)
                if b in a:
                    count = count + a[b]

        
        return count


        


        