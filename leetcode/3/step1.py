class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_last_index = {}
        max_length = 0
        start = 0

        for end, c in enumerate(s):
            if c in char_to_last_index:
                start = max(start, char_to_last_index.pop(c) + 1)
            char_to_last_index[c] = end
            max_length = max(max_length, end - start + 1)

        return max_length
