class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        element1, element2 = None, None
        count1, count2 = 0, 0

        for i in nums:

            if i == element1:
                count1 = count1 + 1
            elif i == element2:
                count2 = count2 + 1
            elif count1 == 0:
                element1 = i
                count1 = 1
            elif count2 == 0:
                element2 = i
                count2 = 1
            else:
                count1 = count1 - 1
                count2 = count2 - 1

        count1, count2 = 0, 0

        for i in nums:
            if i == element1:
                count1 += 1
            elif i == element2:
                count2 += 1
        
        result = []
        if count1 > len(nums) // 3:
            result.append(element1)
        if count2 > len(nums) // 3:
            result.append(element2)

        return result






        

        
        
        
        
        