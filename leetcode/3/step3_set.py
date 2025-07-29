class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        chars_in_use = set()
        for end, char in enumerate(s):
            while char in chars_in_use:
                chars_in_use.remove(s[start])
                start += 1
            chars_in_use.add(char)
            max_length = max(max_length, end - start + 1)
        return max_length
