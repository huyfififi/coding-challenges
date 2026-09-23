class Solution:
    def trap(self, height: list[int]) -> int:
        max_height = max(height)
        max_position = height.index(max_height)

        filled = 0

        prefix_max = float("-inf")
        for i in range(max_position):
            prefix_max = max(prefix_max, height[i])
            filled += prefix_max - height[i]

        suffix_max = float("-inf")
        for i in range(len(height) - 1, max_position, -1):
            suffix_max = max(suffix_max, height[i])
            filled += suffix_max - height[i]

        return filled
