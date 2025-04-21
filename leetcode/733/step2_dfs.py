class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        color_to_replace = image[sr][sc]
        if color_to_replace == color:
            return image

        num_rows, num_cols = len(image), len(image[0])
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def _flood_fill_helper(row: int, col: int) -> None:
            if not (0 <= row < num_rows and 0 <= col < num_cols):
                return
            if image[row][col] != color_to_replace:
                return

            image[row][col] = color

            for row_offset, col_offset in directions:
                _flood_fill_helper(row + row_offset, col + col_offset)

        _flood_fill_helper(sr, sc)
        return image
