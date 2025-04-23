class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        if image[sr][sc] == color:
            return image

        m = len(image)
        n = len(image[0])

        color_to_update = image[sr][sc]
        image[sr][sc] = color

        if sr > 0 and image[sr - 1][sc] == color_to_update:
            self.floodFill(image, sr - 1, sc, color)
        if sr < m - 1 and image[sr + 1][sc] == color_to_update:
            self.floodFill(image, sr + 1, sc, color)
        if sc > 0 and image[sr][sc - 1] == color_to_update:
            self.floodFill(image, sr, sc - 1, color)
        if sc < n - 1 and image[sr][sc + 1] == color_to_update:
            self.floodFill(image, sr, sc + 1, color)

        return image
