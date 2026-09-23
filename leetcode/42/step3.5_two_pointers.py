class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        water_filled = 0
        while left < right:
            if left_max < right_max:
                water_filled += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                water_filled += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])

        return water_filled
