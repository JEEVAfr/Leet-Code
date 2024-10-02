class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sorted_array = sorted(set((arr)))

        hashmap = {}

        for index, number in enumerate(sorted_array):
                hashmap[number] = index + 1
        
        rank = []

        for i in arr:
            rank.append(hashmap[i])
        
        return rank
        