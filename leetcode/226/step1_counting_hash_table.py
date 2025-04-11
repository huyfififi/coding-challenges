from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_count = defaultdict(int)
        t_char_count = defaultdict(int)

        for c in s:
            s_char_count[c] += 1

        for c in t:
            t_char_count[c] += 1

        return s_char_count == t_char_count
