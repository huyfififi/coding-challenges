class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        visited = []
        for i in range(num_rows):
            visited.append([False] * num_cols)

        def explorable(row: int, col: int) -> bool:
            if not (0 <= row < num_rows and 0 <= col < num_cols):
                return False
            return not visited[row][col]

        result = []
        visiting = (0, 0)
        direction_i = 0
        while visiting:
            row, col = visiting
            result.append(matrix[row][col])
            visited[row][col] = True

            row_delta, col_delta = DELTAS[direction_i]
            next_row, next_col = row + row_delta, col + col_delta
            if not explorable(next_row, next_col):
                direction_i = (direction_i + 1) % 4
                row_delta, col_delta = DELTAS[direction_i]
                next_row, next_col = row + row_delta, col + col_delta

            if not explorable(next_row, next_col):
                break
            visiting = (next_row, next_col)

        return result
