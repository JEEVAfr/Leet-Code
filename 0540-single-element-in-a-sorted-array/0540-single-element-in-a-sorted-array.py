class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for key, value in count.items():

            if value == 1:
                return key 


        