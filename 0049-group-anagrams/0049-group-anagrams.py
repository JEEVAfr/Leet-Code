class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for i in strs:
            s = "".join(sorted(i))
            if s not in anagrams:
                anagrams[s] = [i]
            else:
                anagrams[s].append(i)
            
        return list(anagrams.values())

        