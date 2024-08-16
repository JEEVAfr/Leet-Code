class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        current_min = arrays[0][0]
        current_max = arrays[0][-1]

        result = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            result = max(result, abs(arr[-1] - current_min), abs(arr[0] - current_max))
        

            current_min = min(current_min, arr[0])
            current_max = max(current_max, arr[-1])

        return result


        