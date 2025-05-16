import string


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts: list[int] = [0] * 52
        for c in s:
            char_counts[string.ascii_letters.find(c)] += 1

        ans = 0
        center_added = False
        for i in range(52):
            count = char_counts[i]
            if count % 2 == 0:
                ans += count
                continue

            if not center_added:
                ans += count
                center_added = True
                continue

            ans += count - 1

        return ans
