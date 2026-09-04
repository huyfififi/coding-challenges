import collections
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = collections.Counter(t)
        used = 0

        start = 0
        min_start = -math.inf
        min_end = math.inf
        for end in range(1, len(s) + 1):
            if required[s[end - 1]] > 0:
                used += 1
            required[s[end - 1]] -= 1

            while used == len(t):
                if end - start < min_end - min_start:
                    min_start, min_end = start, end

                required[s[start]] += 1
                if required[s[start]] > 0:
                    used -= 1

                start += 1

        if math.isinf(min_end):
            return ""
        return s[min_start:min_end]
