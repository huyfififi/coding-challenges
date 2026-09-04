import collections
import math


def include(c1: collections.Counter, c2: collections.Counter) -> bool:
    for ch in c2:
        if c2[ch] - c1[ch] > 0:
            return False

    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_counter = collections.Counter()
        t_counter = collections.Counter(t)

        substring_start = 0
        substring_end = 0

        min_substring_start = float("-inf")
        min_substring_end = float("inf")

        while substring_start < len(s) and substring_end < len(s):
            while substring_end < len(s) and not include(s_counter, t_counter):
                s_counter[s[substring_end]] += 1
                substring_end += 1

            while substring_start < len(s) and include(s_counter, t_counter):
                if (
                    substring_end - substring_start
                    < min_substring_end - min_substring_start
                ):
                    min_substring_start = substring_start
                    min_substring_end = substring_end
                s_counter[s[substring_start]] -= 1
                substring_start += 1

        if math.isinf(min_substring_end):
            return ""
        return s[min_substring_start:min_substring_end]
