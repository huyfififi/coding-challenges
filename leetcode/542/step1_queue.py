import copy
from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        queue: deque[tuple[int, int, int]] = deque()
        distance_matrix: list[list[int | float]] = copy.deepcopy(mat)
        for row in range(num_rows):
            for col in range(num_cols):
                if distance_matrix[row][col] != 0:
                    distance_matrix[row][col] = float("inf")
                    continue
                queue.append((row - 1, col, 1))
                queue.append((row + 1, col, 1))
                queue.append((row, col - 1, 1))
                queue.append((row, col + 1, 1))

        while queue:
            row_update, col_update, distance = queue.popleft()
            if not (0 <= row_update < num_rows and 0 <= col_update < num_cols):
                continue
            if distance_matrix[row_update][col_update] <= distance:
                continue

            distance_matrix[row_update][col_update] = distance
            queue.append((row_update - 1, col_update, distance + 1))
            queue.append((row_update + 1, col_update, distance + 1))
            queue.append((row_update, col_update - 1, distance + 1))
            queue.append((row_update, col_update + 1, distance + 1))

        return distance_matrix
