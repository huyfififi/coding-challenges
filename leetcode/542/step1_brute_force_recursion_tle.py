import copy


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        distance_matrix = copy.deepcopy(mat)
        for row in range(num_rows):
            for col in range(num_cols):
                if distance_matrix[row][col] > 0:
                    distance_matrix[row][col] = float("inf")

        def propagate_distance(row: int, col: int, distance: int) -> None:
            if not (0 <= row < num_rows and 0 <= col < num_cols):
                return

            if distance_matrix[row][col] <= distance:
                return

            distance_matrix[row][col] = distance
            propagate_distance(row - 1, col, distance + 1)
            propagate_distance(row + 1, col, distance + 1)
            propagate_distance(row, col - 1, distance + 1)
            propagate_distance(row, col + 1, distance + 1)

        for row in range(num_rows):
            for col in range(num_cols):
                if distance_matrix[row][col] != 0:
                    continue
                propagate_distance(row - 1, col, 1)
                propagate_distance(row + 1, col, 1)
                propagate_distance(row, col - 1, 1)
                propagate_distance(row, col + 1, 1)

        return distance_matrix
