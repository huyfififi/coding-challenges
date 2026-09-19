class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        prefix_max = height[left]
        suffix_max = height[right]

        filled = 0
        while left < right:
            if prefix_max < suffix_max:
                filled += prefix_max - height[left]
                left += 1
                prefix_max = max(prefix_max, height[left])
            else:
                filled += suffix_max - height[right]
                right -= 1
                suffix_max = max(suffix_max, height[right])

        return filled
