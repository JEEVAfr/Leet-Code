class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirstPosition(nums, target):
        # first occurence
            l = 0
            r = len(nums) - 1
            first_occurrence = -1
        
            while l <= r :

                mid = (l + r) // 2


                if nums[mid] > target:
                    r = mid - 1

                elif nums[mid] < target:
                    l = mid + 1

                else: 
                    first_occurrence = mid
                    right = mid - 1

                    r = mid - 1

            return first_occurrence

        def findLastPosition(nums, target):
        # last occurence
            l = 0
            r = len(nums) - 1
            last_occurence = -1

            while l <= r :

                mid = (l + r) // 2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    last_occurence = mid
                    l = mid + 1
        
            return last_occurence
    
        first = findFirstPosition(nums, target)
        last = findLastPosition(nums, target)
        
        
        return [first, last] 

        


        
