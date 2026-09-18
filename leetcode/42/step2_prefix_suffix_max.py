class Solution:
    def trap(self, height: list[int]) -> int:
        prefix_max = [float("-inf")] * len(height)
        prefix_max[0] = height[0]
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i - 1], height[i])

        suffix_max = [float("-inf")] * len(height)
        suffix_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        filled = 0
        for i in range(len(height)):
            capped_height = min(prefix_max[i], suffix_max[i])
            filled += capped_height - height[i]

        return filled
