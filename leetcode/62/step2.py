class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    count[row][col] = 1
                    continue

                count[row][col] = count[row - 1][col] + count[row][col - 1]

        return count[m - 1][n - 1]
