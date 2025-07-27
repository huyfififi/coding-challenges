class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 1:
                    mat[row][col] = float("inf")

        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    continue
                if row > 0:
                    mat[row][col] = min(mat[row][col], mat[row - 1][col] + 1)
                if col > 0:
                    mat[row][col] = min(mat[row][col], mat[row][col - 1] + 1)

        for row in range(num_rows - 1, -1, -1):
            for col in range(num_cols - 1, -1, -1):
                if mat[row][col] == 0:
                    continue
                if row < num_rows - 1:
                    mat[row][col] = min(mat[row][col], mat[row + 1][col] + 1)
                if col < num_cols - 1:
                    mat[row][col] = min(mat[row][col], mat[row][col + 1] + 1)

        return mat
