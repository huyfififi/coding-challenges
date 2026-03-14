class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [1] * n
        for _ in range(1, m):
            for col in range(1, n):
                count[col] += count[col - 1]
        return count[-1]
