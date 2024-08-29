class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L = L + 1

            if nums[R] in window:
                return True
            else:
                window.add(nums[R])


        