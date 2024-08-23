class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        paired = []
        for i in nums:
            if i % 2 == 0:
                paired.append(i)
        
        req = []
        count = Counter(paired)

        for i in count:
            if count[i]==max(count.values()):
                req.append(i)

        if len(paired) == 0:
            return -1

        return min(req)
        
        

       

        