class Solution:
    def longestPalindrome(self, s: str) -> str:
        # is_palindrome[start][end] is True -> s[start:end + 1] is a palindrome
        is_palindrome = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            is_palindrome[i][i] = True

        max_length = 1
        max_start = 0
        max_end = 0
        for start in range(len(s) - 1, -1, -1):
            for end in range(start, len(s)):
                if (
                    s[start] == s[end]
                    and (
                        end - start + 1 <= 2 or is_palindrome[start + 1][end - 1]
                    )
                ):
                    is_palindrome[start][end] = True
                    if end - start + 1 > max_length:
                        max_length = end - start + 1
                        max_start = start
                        max_end = end

        return s[max_start:max_end + 1]
