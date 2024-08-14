class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_s = {}

        for i in nums:
            count_s[i] = count_s.get(i, 0) + 1

        
        for key, value in count_s.items():
            if value > len(nums) // 2:
                return key
        
        
        


        