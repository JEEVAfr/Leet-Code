class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        
        if len(nums) > 1:
            middle = len(nums) // 2

            left = self.sortArray(nums[:middle])  # Recursively sort the left half
            right = self.sortArray(nums[middle:])  # Recursively sort the right half

            left_pointer = 0
            right_pointer = 0
            check_pointer = 0

    
            while left_pointer < len(left) and right_pointer < len(right):
                if left[left_pointer] < right[right_pointer]:
                    nums[check_pointer] = left[left_pointer]
                    left_pointer += 1
                else:
                    nums[check_pointer] = right[right_pointer]
                    right_pointer += 1
                check_pointer += 1

  
          
            while left_pointer < len(left):
                nums[check_pointer] = left[left_pointer]
                left_pointer += 1
                check_pointer += 1
        
            while right_pointer < len(right):
                nums[check_pointer] = right[right_pointer]
                right_pointer += 1
                check_pointer += 1

        return nums

       