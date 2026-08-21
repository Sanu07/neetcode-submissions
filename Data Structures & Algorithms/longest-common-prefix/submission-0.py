class Solution:

    def _get_min_length(self, strs: List[str]) -> str:
        return min(strs, key=len)


    def _longestCommonPrefix1(self, strs: List[str]) -> str:
        min_len_str: str = self._get_min_length(strs)
        min_len: int = len(min_len_str)
        parts = []
        for i in range(min_len):
            first_char: str = min_len_str[i]
            is_same: bool = True
            for j in range(len(strs)):
                if strs[j][i] != first_char:
                    is_same = False
                    break
            if is_same:
                parts.append(min_len_str[i])
            else:
                break
        return ''.join(parts)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self._longestCommonPrefix1(strs)