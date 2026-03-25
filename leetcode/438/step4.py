class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        p_count = [0] * 26
        s_count = [0] * 26
        for i in range(len(p)):
            p_count[ord(p[i]) - ord("a")] += 1
            s_count[ord(s[i]) - ord("a")] += 1

        anagram_starts = []
        for checking_start in range(len(s) - len(p) + 1):
            if s_count == p_count:
                anagram_starts.append(checking_start)

            if checking_start < len(s) - len(p):
                s_count[ord(s[checking_start]) - ord("a")] -= 1
                s_count[ord(s[checking_start + len(p)]) - ord("a")] += 1

        return anagram_starts
