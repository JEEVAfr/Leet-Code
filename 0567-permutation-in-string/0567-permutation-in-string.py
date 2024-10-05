class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        left = 0
        right = 0

        s1_count = Counter(s1)

        window_count = Counter()

        while right < len(s2):

            window_count[s2[right]] += 1    

            if right - left + 1 < k:
                right += 1
            
            else:
                if window_count == s1_count:
                    return True
                
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
            
                left += 1
                right += 1



        return False
        