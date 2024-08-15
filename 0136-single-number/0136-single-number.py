class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #counter = {}

        #for i in nums:
        #   counter[i] = counter.get(i, 0) + 1
        

        #for key, value in counter.items():
        #    if value == 1: # 0(n) time
        #        return key # 0(n) space


        unique = 0

        for i in nums:
            unique = unique ^ i
        return unique       #0(n) - time
                            #0(1) - space

                            

        
        

