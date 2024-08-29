class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        tortize = nums[0]
        hare = nums[0]

        while True:

            tortize = nums[tortize] # move 1 step
            hare = nums[nums[hare]] # move 2 step


            # eventually meet
            if tortize == hare:
                break

        tortize = nums[0]

        while tortize != hare:

            tortize = nums[tortize] 
            hare = nums[hare]

        return tortize










        