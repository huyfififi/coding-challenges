from collections import deque


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        color_to_update = image[sr][sc]
        if color_to_update == color:
            return image

        queue = deque([(sr, sc)])
        num_rows, num_cols = len(image), len(image[0])

        while queue:
            row, col = queue.popleft()

            if not (0 <= row < num_rows and 0 <= col < num_cols):
                continue
            if image[row][col] != color_to_update:
                continue

            image[row][col] = color
            queue.append((row - 1, col))
            queue.append((row + 1, col))
            queue.append((row, col - 1))
            queue.append((row, col + 1))

        return image
