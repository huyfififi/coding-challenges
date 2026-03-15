class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_count = [[0] * n for _ in range(m)]
        for i in range(m):
            path_count[i][0] = 1
        for i in range(n):
            path_count[0][i] = 1

        for row in range(1, m):
            for col in range(1, n):
                path_count[row][col] = (
                    path_count[row - 1][col] + path_count[row][col - 1]
                )

        return path_count[m - 1][n - 1]
