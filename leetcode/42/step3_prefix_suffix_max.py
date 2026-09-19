class Solution:
    def trap(self, height: list[int]) -> int:
        prefix_max = height.copy()
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i - 1], height[i])

        suffix_max = height.copy()
        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        filled = 0
        for i in range(len(height)):
            filled += min(prefix_max[i], suffix_max[i]) - height[i]

        return filled
