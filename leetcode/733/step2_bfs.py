from collections import deque


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        color_to_update = image[sr][sc]
        if color_to_update == color:
            return image

        num_rows = len(image)
        num_cols = len(image[0])

        queue = deque([(sr, sc)])
        while queue:
            row, col = queue.popleft()
            image[row][col] = color

            if row > 0 and image[row - 1][col] == color_to_update:
                queue.append((row - 1, col))
            if row < num_rows - 1 and image[row + 1][col] == color_to_update:
                queue.append((row + 1, col))
            if col > 0 and image[row][col - 1] == color_to_update:
                queue.append((row, col - 1))
            if col < num_cols - 1 and image[row][col + 1] == color_to_update:
                queue.append((row, col + 1))

        return image
