from collections import deque


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        color_to_update = image[sr][sc]
        if color_to_update == color:
            return image

        queue = deque([(sr, sc)])
        while queue:
            pix_row, pix_col = queue.popleft()
            image[pix_row][pix_col] = color

            if pix_row > 0 and image[pix_row - 1][pix_col] == color_to_update:
                queue.append((pix_row - 1, pix_col))
            if pix_row < m - 1 and image[pix_row + 1][pix_col] == color_to_update:
                queue.append((pix_row + 1, pix_col))
            if pix_col > 0 and image[pix_row][pix_col - 1] == color_to_update:
                queue.append((pix_row, pix_col - 1))
            if pix_col < n - 1 and image[pix_row][pix_col + 1] == color_to_update:
                queue.append((pix_row, pix_col + 1))

        return image
