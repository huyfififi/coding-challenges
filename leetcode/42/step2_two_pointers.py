class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max_height = height[left]
        right_max_height = height[right]

        filled = 0
        while left < right:
            if left_max_height < right_max_height:
                filled += left_max_height - height[left]
                left += 1
                left_max_height = max(left_max_height, height[left])
            else:
                filled += right_max_height - height[right]
                right -= 1
                right_max_height = max(right_max_height, height[right])

        return filled
