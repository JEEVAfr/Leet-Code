class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        count_1 = {}
        count_2 = {}

        for i in words1:
            count_1[i] = count_1.get(i, 0) + 1
        
        for j in words2:
            count_2[j] = count_2.get(j, 0) + 1
        
        count = 0

        for i in count_1:
            if count_1[i] == 1 and count_2.get(i, 0) == 1:
                count += 1
            
        
        return count


        