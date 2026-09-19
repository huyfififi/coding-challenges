class Solution:
    def trap(self, height: list[int]) -> int:
        max_height = max(height)
        max_position = height.index(max_height)

        filled = 0

        left_max = float("-inf")
        for left in range(max_position):
            left_max = max(left_max, height[left])
            filled += left_max - height[left]

        right_max = float("-inf")
        for right in range(len(height) - 1, max_position, -1):
            right_max = max(right_max, height[right])
            filled += right_max - height[right]

        return filled
