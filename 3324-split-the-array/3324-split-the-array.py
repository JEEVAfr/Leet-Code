class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for i in count.values():

            if i > 2:
                return False
        
        return True
        

        

        