from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = defaultdict(int)
        for c in s:
            char_counts[c] += 1

        palindrome_length = 0
        has_odd_count = False
        for _, count in char_counts.items():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                has_odd_count = True

        if has_odd_count:
            palindrome_length += 1

        return palindrome_length
