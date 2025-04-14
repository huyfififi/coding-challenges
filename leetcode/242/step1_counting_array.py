class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = [0] * 26
        t_counter = [0] * 26

        for c in s:
            s_counter[ord(c) - ord("a")] += 1

        for c in t:
            t_counter[ord(c) - ord("a")] += 1

        for i in range(26):
            if s_counter[i] != t_counter[i]:
                return False

        return True
