from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = Counter(s)

        palindrome_length = 0
        has_odd_count = False
        for count in char_counts.values():
            palindrome_length += count - count % 2
            has_odd_count |= count % 2 == 1

        if has_odd_count:
            palindrome_length += 1
        return palindrome_length
