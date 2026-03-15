class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        result = []
        visited = [[False] * num_cols for _ in range(num_rows)]
        row, col = 0, 0
        direction_i = 0
        for _ in range(num_rows * num_cols):
            result.append(matrix[row][col])
            visited[row][col] = True

            row_delta, col_delta = DIRECTIONS[direction_i]
            if (
                not (
                    0 <= row + row_delta < num_rows and 0 <= col + col_delta < num_cols
                )
                or visited[row + row_delta][col + col_delta]
            ):
                direction_i = (direction_i + 1) % 4

            row_delta, col_delta = DIRECTIONS[direction_i]
            row += row_delta
            col += col_delta

        return result
