class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_palindrome = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            is_palindrome[i][i] = True

        max_start = 0
        max_length = 1
        for start in range(len(s) - 1, -1, -1):
            for end in range(start, len(s)):
                if s[start] != s[end]:
                    continue

                length = end - start + 1
                if length > 2 and not is_palindrome[start + 1][end - 1]:
                    continue

                is_palindrome[start][end] = True
                if length > max_length:
                    max_start = start
                    max_length = length

        return s[max_start : max_start + max_length]
