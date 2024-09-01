class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        even = 0
        odd = 1

        for i in nums:
            if i > 0:
                result[even] = i
                even = even + 2
            else:
                result[odd] = i
                odd = odd + 2
            
        return result



        