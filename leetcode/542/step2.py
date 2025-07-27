import math
from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        queue: deque[tuple[int, int]] = deque()
        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = math.inf

        directions: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            row, col = queue.popleft()
            distance = mat[row][col]

            for row_diff, col_diff in directions:
                row_update = row + row_diff
                col_update = col + col_diff

                if (
                    0 <= row_update < num_rows
                    and 0 <= col_update < num_cols
                    and mat[row_update][col_update] > distance + 1
                ):
                    mat[row_update][col_update] = distance + 1
                    queue.append((row_update, col_update))

        return mat
