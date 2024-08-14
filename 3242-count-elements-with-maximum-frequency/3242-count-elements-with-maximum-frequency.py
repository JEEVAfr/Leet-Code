class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = {}
        total = []

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        
        
        for key, value in counter.items():
            total.append(value)

        max_num = max(total) # 2
        return max_num * total.count(max_num) # count function is used to count how many 2 in the list.

