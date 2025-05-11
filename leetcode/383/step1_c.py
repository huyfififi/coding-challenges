class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Leverage input contains only lowercase English letters
        necessary_counts = [0] * 26
        available_counts = [0] * 26

        for c in ransomNote:
            necessary_counts[ord(c) - ord("a")] += 1
        for c in magazine:
            available_counts[ord(c) - ord("a")] += 1

        for i in range(26):
            if necessary_counts[i] > available_counts[i]:
                return False
        return True
