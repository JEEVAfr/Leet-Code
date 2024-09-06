class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count_note = {}
        count_magazine = {}

        for i in ransomNote:
            count_note[i] = count_note.get(i, 0) + 1

        for j in magazine:
            count_magazine[j] = count_magazine.get(j, 0) + 1

        for char in count_note:
            if count_magazine.get(char, 0) < count_note[char]:
                return False
        
        return True
        