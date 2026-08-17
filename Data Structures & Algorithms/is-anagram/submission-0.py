class Solution:
    
    def _count_characters(self, char_count: dict, val: str):
        for char in val:
            char_count[char] = char_count.get(char, 0) + 1
    
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = {}
        char_count_t = {}
        self._count_characters(char_count_s, s)
        self._count_characters(char_count_t, t)
        return char_count_s == char_count_t
    


        