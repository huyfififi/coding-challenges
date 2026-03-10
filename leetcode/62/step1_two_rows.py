class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n
        for row in range(1, m):
            curr_row = [0] * n
            for col in range(n):
                if col == 0:
                    curr_row[col] = 1
                    continue

                curr_row[col] = curr_row[col - 1] + prev_row[col]

            prev_row = curr_row

        return prev_row[-1]
