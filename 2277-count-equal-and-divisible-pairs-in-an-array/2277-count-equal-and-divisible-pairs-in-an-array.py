class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        index_dict = defaultdict(list)
        
        for index, value in enumerate(nums):
            index_dict[value].append(index)
        
        count = 0

        for indx in index_dict.values():

            for i in range(len(indx)):
                for j in range(i + 1, len(indx)):

                    if (indx[i] * indx[j]) % k == 0:
                        count = count + 1

        return count

