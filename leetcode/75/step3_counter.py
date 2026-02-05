class Solution:
    def sortColors(self, nums: list[int]) -> None:
        RED = 0
        WHITE = 1
        BLUE = 2

        counts = [0, 0, 0]
        for color in nums:
            counts[color] += 1

        filling = 0

        def fill_color(color: int) -> None:
            nonlocal filling

            while counts[color] > 0:
                nums[filling] = color
                counts[color] -= 1
                filling += 1

        fill_color(RED)
        fill_color(WHITE)
        fill_color(BLUE)
