class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        color_to_update = image[sr][sc]
        if color_to_update == color:
            return image

        num_rows = len(image)
        num_cols = len(image[0])

        image[sr][sc] = color
        if sr > 0 and image[sr - 1][sc] == color_to_update:
            self.floodFill(image, sr - 1, sc, color)
        if sr < num_rows - 1 and image[sr + 1][sc] == color_to_update:
            self.floodFill(image, sr + 1, sc, color)
        if sc > 0 and image[sr][sc - 1] == color_to_update:
            self.floodFill(image, sr, sc - 1, color)
        if sc < num_cols - 1 and image[sr][sc + 1] == color_to_update:
            self.floodFill(image, sr, sc + 1, color)

        return image
