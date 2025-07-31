class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        char_to_last_index = {}
        max_length = 0
        for end, char in enumerate(s):
            if char in char_to_last_index:
                start = max(start, char_to_last_index[char] + 1)
            char_to_last_index[char] = end
            max_length = max(max_length, end - start + 1)
        return max_length
