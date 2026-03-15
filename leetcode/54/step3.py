class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        visited = []
        for _ in range(num_rows):
            visited.append([False] * num_cols)

        row, col = 0, 0
        row_delta, col_delta = 0, 1
        result = []
        for _ in range(num_rows * num_cols):
            result.append(matrix[row][col])
            visited[row][col] = True

            if (
                not (
                    0 <= row + row_delta < num_rows and 0 <= col + col_delta < num_cols
                )
                or visited[row + row_delta][col + col_delta]
            ):
                row_delta, col_delta = col_delta, -row_delta

            row = row + row_delta
            col = col + col_delta

        return result
