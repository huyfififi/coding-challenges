# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_i = 1
        right_i = n

        while left_i < right_i:
            middle_i = (left_i + right_i) // 2
            if isBadVersion(middle_i):
                right_i = middle_i
            else:
                left_i = middle_i + 1

        assert left_i == right_i
        return right_i
