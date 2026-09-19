class Solution:
    def trap(self, height: list[int]) -> int:
        max_height = max(height)
        max_position = height.index(max_height)

        trapped = 0

        left_max = height[0]
        for i in range(1, max_position):
            left_max = max(left_max, height[i])
            trapped += left_max - height[i]

        right_max = height[-1]
        for i in range(len(height) - 2, max_position, -1):
            right_max = max(right_max, height[i])
            trapped += right_max - height[i]

        return trapped
