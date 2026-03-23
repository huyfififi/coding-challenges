import string


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        p_count = [0] * 26
        for c in p:
            p_count[string.ascii_lowercase.find(c)] += 1

        s_count = [0] * 26
        for i in range(len(p)):
            s_count[string.ascii_lowercase.find(s[i])] += 1

        anagram_starts: list[int] = []
        for checking_start in range(len(s) - len(p) + 1):
            if s_count == p_count:
                anagram_starts.append(checking_start)

            if checking_start < len(s) - len(p):
                s_count[string.ascii_lowercase.find(s[checking_start])] -= 1
                s_count[string.ascii_lowercase.find(s[checking_start + len(p)])] += 1

        return anagram_starts
