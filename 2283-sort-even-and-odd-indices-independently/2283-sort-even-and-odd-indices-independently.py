class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [nums[i] for i in range(0, len(nums), 2)]
        odd = [nums[i] for i in range(1, len(nums), 2)]

        even.sort()
        odd.sort(reverse = True)

        result = []
        left = 0
        right = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[left])
                left = left + 1
            
            else:
                result.append(odd[right])
                right = right + 1

        return result

        