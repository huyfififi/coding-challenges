import collections
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = collections.Counter(t)
        used = 0

        start = 0
        min_start = 0
        min_size = math.inf
        for end in range(len(s)):
            if required[s[end]] > 0:
                used += 1
            required[s[end]] -= 1

            while used == len(t):
                if end - start + 1 < min_size:
                    min_start, min_size = start, end - start + 1

                required[s[start]] += 1
                if required[s[start]] > 0:
                    used -= 1
                start += 1

        if math.isinf(min_size):
            return ""
        return s[min_start : min_start + min_size]
