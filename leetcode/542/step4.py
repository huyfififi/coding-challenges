import copy
import math


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        distances = copy.deepcopy(mat)
        for row in range(num_rows):
            for col in range(num_cols):
                if distances[row][col] != 0:
                    distances[row][col] = math.inf

        updated = True
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while updated:
            updated = False
            for row in range(num_rows):
                for col in range(num_cols):
                    for dr, dc in directions:
                        neighbor_row = row + dr
                        neighbor_col = col + dc
                        if not (
                            0 <= neighbor_row < num_rows
                            and 0 <= neighbor_col < num_cols
                        ):
                            continue

                        if (
                            distances[neighbor_row][neighbor_col]
                            > distances[row][col] + 1
                        ):
                            distances[neighbor_row][neighbor_col] = (
                                distances[row][col] + 1
                            )
                            updated = True

        return distances
