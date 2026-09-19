class Solution:
    def trap(self, height: list[int]) -> int:
        max_height = max(height)
        max_position = height.index(max_height)

        filling = 0

        checking_height = height[0]
        left = 1
        while left < max_position:
            if checking_height < height[left]:  # ruff: Replace with `max` call
                checking_height = height[left]

            filling += checking_height - height[left]
            left += 1

        checking_height = height[-1]
        right = len(height) - 2
        while max_position < right:
            if checking_height < height[right]:
                checking_height = height[right]

            filling += checking_height - height[right]
            right -= 1

        return filling
