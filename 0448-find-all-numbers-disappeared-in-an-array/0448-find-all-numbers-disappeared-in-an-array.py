class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i in a:
                continue
            else:
                result.append(i)
            
        return result

            
             
        