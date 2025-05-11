class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def _char_to_index(c: str) -> int:
            return ord(c) - ord("a")

        available_counts = [0] * 26

        for c in magazine:
            available_counts[_char_to_index(c)] += 1

        for c in ransomNote:
            index = _char_to_index(c)
            available_counts[index] -= 1
            if available_counts[index] < 0:
                return False

        return True
