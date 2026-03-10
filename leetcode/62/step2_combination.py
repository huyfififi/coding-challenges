class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = max(m, n), min(m, n)

        numerator = 1
        denominator = 1
        for i in range(n - 1):
            numerator *= m + n - 2 - i
            denominator *= n - 1 - i

        return numerator // denominator
